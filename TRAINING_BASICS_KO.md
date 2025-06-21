# LLVC 훈련 기본 가이드

이 문서는 개인 음성(타깃 스피커)의 WAV 파일을 사용해 LLVC 모델을 학습하는 방법을 초심자에게 설명합니다.

## 1. 데이터셋 구조

훈련 데이터 폴더는 `train`, `val`, `dev` 세 개의 하위 폴더로 구성됩니다. 각 폴더 안에는 아래와 같은 WAV 쌍이 존재해야 합니다.

- `PREFIX_original.wav`: 다양한 화자가 녹음한 음성
- `PREFIX_converted.wav`: `PREFIX_original.wav`을 타깃 스피커의 목소리로 변환한 파일

`*_original.wav`과 `*_converted.wav`가 같은 이름을 갖도록 맞춰야 합니다.

## 2. 타깃 스피커 음성으로 데이터 준비하기

타깃 스피커의 WAV 파일만 있는 경우 `minimal_rvc/_infer_folder.py` 스크립트를 이용해 공개 데이터셋을 원하는 목소리로 변환할 수 있습니다. 예시는 다음과 같습니다.

```bash
python -m minimal_rvc._infer_folder \
    --train_set_path "LibriSpeech/train-clean-360" \
    --dev_set_path "LibriSpeech/dev-clean" \
    --out_path "f_8312_ls360" \
    --flatten \
    --model_path "llvc_models/models/rvc/f_8312_32k-325.pth" \
    --model_name "f_8312" \
    --target_sr 16000 \
    --f0_method "rmvpe" \
    --val_percent 0.02 \
    --random_seed 42 \
    --f0_up_key 12
```

위 명령은 LibriSpeech의 데이터를 타깃 목소리로 변환해 `f_8312_ls360` 폴더에 `train`, `dev`, `val` 하위 폴더를 생성합니다. 이렇게 얻은 폴더를 `config.json`의 `data.dir`에 지정하면 됩니다.

## 3. 설정 파일 만들기

1. `experiments/my_run` 폴더를 생성한 뒤 `experiments/llvc/config.json`을 복사합니다.
2. 복사한 `config.json`에서 `"data": { "dir": "..." }` 값을 위에서 준비한 데이터셋 경로로 수정합니다.
3. 필요 시 다른 하이퍼파라미터도 조정합니다.

## 4. 훈련 실행

가상 환경을 활성화한 후 다음 명령으로 학습을 시작합니다.

```bash
python train.py -d experiments/my_run
```

체크포인트와 로그는 `experiments/my_run/checkpoints`와 `experiments/my_run/logs`에 저장되며, TensorBoard로 학습 과정을 확인할 수 있습니다.

## 5. 훈련 중단 후 재개

`train.py`는 가장 최근의 체크포인트를 자동으로 불러와 이어서 학습합니다. 실행 디렉터리와 `config.json`을 그대로 두면 중단된 시점부터 계속 학습됩니다.

## 마무리
이제 타깃 스피커의 WAV 파일을 활용해 LLVC 모델을 훈련할 수 있습니다. 데이터 준비와 설정 파일 위치만 잘 맞추면 `train.py` 하나로 전체 학습 과정을 진행할 수 있습니다.
