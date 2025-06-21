# LLVC 설치 입문 가이드

이 문서는 AI나 머신러닝을 전혀 모르는 사용자를 대상으로 LLVC(저지연 음성 변환) 프로젝트를 설치하는 방법을 설명합니다.

## 1. 파이썬 설치

1. [아나콘다](https://www.anaconda.com/download)에서 운영체제에 맞는 버전을 다운로드하여 설치합니다. 아나콘다는 프로젝트별로 독립된 "환경"을 만들 수 있게 해 줍니다.
2. **Anaconda Prompt**(윈도우) 또는 터미널(macOS/Linux)을 엽니다.

## 2. 가상 환경 만들기

`llvc`라는 이름의 파이썬 환경을 만들고 활성화합니다:

```bash
conda create -n llvc python=3.11
conda activate llvc
```

## 3. 파이토치 설치

[파이토치 설치 페이지](https://pytorch.org/get-started/locally/)에서 본인 시스템에 맞는 명령어를 확인합니다. 해당 명령을 위에서 만든 `llvc` 환경에서 실행해 **torch**와 **torchaudio**를 설치합니다.

## 4. 추가 패키지 설치

`llvc` 환경이 활성화된 상태에서 다음 명령으로 프로젝트 의존성을 설치합니다:

```bash
pip install -r requirements.txt
```

## 5. 사전 학습 모델 다운로드

프로젝트에 포함된 스크립트를 실행해 필요한 모델 파일을 내려받습니다:

```bash
python download_models.py
```

실행 후 `llvc_models` 폴더에 모델이 저장됩니다.

## 6. 설치 확인

예시 오디오 파일을 변환해 보며 설치가 제대로 되었는지 확인합니다:

```bash
python infer.py
```

변환된 파일은 `converted_out` 폴더에 저장됩니다.

## 7. (선택 사항) 평가 도구 사용

`eval.py`를 실행하려면 별도의 파이썬 3.9 환경을 만들어야 합니다:

```bash
conda create -n llvc-eval python=3.9
conda activate llvc-eval
pip install -r eval_requirements.txt
```

## 다음 단계

* 자신만의 오디오 파일을 변환하려면 `python infer.py -p my_checkpoint.pth -c my_config.json -f path/to/audio` 명령을 사용하세요. 자세한 옵션은 `README.md`를 참고합니다.
* 간단한 웹 인터페이스를 이용하려면 `python webui/app.py`를 실행하고 브라우저에서 `http://localhost:8000`을 엽니다.

이제 LLVC가 준비되었습니다. 다양한 음성 변환을 실험해 보세요.
