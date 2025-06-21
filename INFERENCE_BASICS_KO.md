# LLVC 추론(음성 변환) 기본 가이드

이 문서는 LLVC에서 제공하는 모델을 사용하여 새로운 음성 파일을 만드는 방법을 초심자에게 설명합니다.

## 1. 준비 단계
이미 설치가 완료되어 있고 사전 학습 모델을 다운로드했다고 가정합니다. `llvc` 환경을 활성화한 뒤 프로젝트 루트에서 다음 명령들을 실행하세요.

## 2. 기본 명령
샘플 오디오(`test_wavs` 폴더)에 대해 변환을 실행하려면:

```bash
python infer.py
```

변환된 파일은 `converted_out` 폴더에 저장됩니다.

## 3. 내 파일 변환하기
`-f` 옵션에 변환하고 싶은 파일을 지정하고, `-o` 옵션으로 결과가 저장될 폴더를 설정할 수 있습니다.

```bash
python infer.py -f path/to/input.wav -o my_results
```

## 4. 체크포인트와 설정 파일 변경하기
다른 체크포인트나 설정 파일을 사용하려면 `-p`와 `-c` 옵션을 지정합니다.

```bash
python infer.py -p llvc_models/models/checkpoints/llvc/G_500000.pth -c experiments/llvc/config.json -f input.wav
```

## 5. 스트리밍 모드
스트리밍 환경을 시뮬레이션하려면 `-s` 옵션과 함께 `-n`으로 청크 배수를 지정합니다. 청크가 작을수록 지연은 짧아지지만 품질에 영향을 줄 수 있습니다.

```bash
python infer.py -f input.wav -s -n 2
```

실행 후 터미널에 실시간비(real-time factor)와 지연 시간이 출력됩니다.

## 6. 여러 파일 한 번에 변환하기
폴더를 지정하면 그 안의 모든 WAV 파일이 변환됩니다.

```bash
python infer.py -f my_wavs -o outputs
```

## 7. RVC 모델로 변환하기
LLVC 외에 RVC 모델로도 음성 변환을 수행할 수 있습니다. `compare_infer.py` 스크립트를 사용하면 기본 제공 RVC 모델을 로드하여 변환을 실행할 수 있습니다.

### 단일 파일 예시

```bash
python compare_infer.py -f input.wav -m rvc -o rvc_results
```

### 폴더 전체 변환 예시

```bash
python compare_infer.py -f my_wavs -m rvc -o rvc_results
```

`-m rvc` 옵션을 통해 RVC 모델(`llvc_models/models/rvc_no_f0/f_8312_no_f0-300.pth`)을 사용하며, `--window_ms` 등 추가 파라미터로 스트리밍 설정을 조절할 수 있습니다.

## 마무리
이제 위 예시들을 바탕으로 원하는 오디오 파일을 자유롭게 변환해 보세요. 사용 가능한 모든 옵션은 `python infer.py -h` 명령으로 확인할 수 있습니다.

