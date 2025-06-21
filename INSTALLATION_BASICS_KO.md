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

`llvc` 환경이 활성화된 상태에서 프로젝트 의존성을 설치합니다. Ubuntu나 Debian
리눅스 사용자라면 먼저 C++ 컴파일러가 포함된 패키지를 설치하세요. `fairseq`와
`pyworld`는 C++ 확장 모듈을 빌드하므로 g++가 없으면 오류가 발생합니다:

```bash
sudo apt update
sudo apt install build-essential
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

평가 도구는 모델의 성능을 측정하기 위해 사용하는 스크립트입니다. 단순히 제공된
모델을 사용해 음성을 변환하고 싶다면 이 단계는 건너뛰어도 됩니다. 사용을 원한다면
다음과 같이 별도의 파이썬 3.9 환경을 만듭니다:

```bash
conda create -n llvc-eval python=3.9
conda activate llvc-eval
pip install -r eval_requirements.txt
```

## 8. 웹 UI 사용하기

이 프로젝트에는 Flask 기반의 간단한 웹 인터페이스가 포함되어 있습니다. 위에서 만든
`llvc` 환경을 활성화한 뒤 다음 명령으로 서버를 실행합니다:

```bash
python webui/app.py
```

브라우저에서 <http://localhost:8000> 주소를 열고 오디오 파일을 업로드하면 자동으
로 변환이 진행됩니다. 완료되면 다운로드 링크가 표시됩니다. 서버를 종료하려면 터미
널에서 `Ctrl+C`를 누르세요.

## 다음 단계

* 자신만의 오디오 파일을 변환하려면 `python infer.py -p my_checkpoint.pth -c my_config.json -f path/to/audio` 명령을 사용하세요. 자세한 옵션은 `README.md`를 참고합니다.

이제 LLVC가 준비되었습니다. 다양한 음성 변환을 실험해 보세요.
