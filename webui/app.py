import os
import uuid
import threading
from flask import Flask, request, jsonify, send_file, render_template
from infer import load_model, load_audio, save_audio, do_infer

app = Flask(__name__)

CHECKPOINT = os.getenv('LLVC_CHECKPOINT', 'llvc_models/models/checkpoints/llvc/G_500000.pth')
CONFIG = os.getenv('LLVC_CONFIG', 'experiments/llvc/config.json')

model = None
sample_rate = 16000

# simple job store
jobs = {}

class Job:
    def __init__(self, job_id):
        self.id = job_id
        self.status = 'processing'
        self.out_path = None

def worker(job_id, audio_path, stream=False, chunk_factor=1):
    global model, sample_rate
    try:
        if model is None:
            model, sample_rate = load_model(CHECKPOINT, CONFIG)
        audio = load_audio(audio_path, sample_rate)
        output, _, _ = do_infer(model, audio, chunk_factor, sample_rate, stream)
        out_dir = os.path.join('webui', 'jobs')
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{job_id}.wav")
        save_audio(output, out_path, sample_rate)
        jobs[job_id].out_path = out_path
        jobs[job_id].status = 'done'
    except Exception as e:
        jobs[job_id].status = 'error'
        jobs[job_id].out_path = str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/models')
def list_models():
    return jsonify([{
        'model_id': 'llvc_default',
        'description': 'Pretrained LLVC model',
        'sample_rate': sample_rate
    }])

@app.route('/api/v1/convert', methods=['POST'])
def convert():
    f = request.files.get('file')
    if not f:
        return jsonify({'error': 'file missing'}), 400
    job_id = str(uuid.uuid4())
    tmp_dir = os.path.join('webui', 'uploads')
    os.makedirs(tmp_dir, exist_ok=True)
    audio_path = os.path.join(tmp_dir, f"{job_id}_{f.filename}")
    f.save(audio_path)
    jobs[job_id] = Job(job_id)
    stream = request.form.get('stream', 'false').lower() == 'true'
    chunk_factor = int(request.form.get('chunk_factor', 1))
    threading.Thread(target=worker, args=(job_id, audio_path, stream, chunk_factor), daemon=True).start()
    return jsonify({'job_id': job_id}), 202

@app.route('/api/v1/jobs/<job_id>')
def job_status(job_id):
    job = jobs.get(job_id)
    if not job:
        return jsonify({'error': 'job not found'}), 404
    return jsonify({'job_id': job_id, 'status': job.status})

@app.route('/api/v1/jobs/<job_id>/result')
def job_result(job_id):
    job = jobs.get(job_id)
    if not job:
        return jsonify({'error': 'job not found'}), 404
    if job.status != 'done':
        return jsonify({'error': 'job not completed'}), 400
    return send_file(job.out_path, as_attachment=True)

@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
