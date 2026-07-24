# Runtime Validation Report

> Date：2026-07-24
>
> Branch：`codex/refactor-curriculum-v2-full-migration`
> Scope：Final Integration & Runtime Correctness Pass

## Status Vocabulary

本報告只使用：Executed、Not validated yet、Hardware blocked、Network blocked、Model access blocked、License blocked、Environment blocked。`compileall` 成功不等於真實模型已執行。

## Compile Validation

- Command：bundled Python equivalent of `python -m compileall -q learning`
- Result：Executed / Passed
- Exit code：0
- Files：active curriculum Python sources；產生的 `__pycache__` 已清除。

## Basic Demo Validation

- Result：Executed / Passed
- Count：36
- Coverage：Week01–02、Week04–16 中所有不需下載大型模型、外部輸入或 ROS2／Isaac Sim 等特殊 runtime 的 `demo/` Python 程式。
- Failed：0
- Note：終端顯示的少數繁體中文亂碼來自 PowerShell code page，不是 Python exception；所有程序 exit code 均為 0。

## Real Track Validation

| Week | Track | Command / API validation | Runtime status | Evidence / blocker |
|---|---|---|---|---|
| Week04 | LLaVA visual QA | CLI、compile、官方 `AutoProcessor` / `LlavaForConditionalGeneration` flow audited | Environment blocked | `torch=False`, `transformers=False`; no model download or GPU runtime attempted |
| Week06 | Qwen2.5-VL video | `--fps` / `--frames` mutually exclusive CLI、official `process_vision_info(..., return_video_kwargs=True)` audited | Environment blocked | `torch=False`, `transformers=False`, `qwen_vl_utils=False`, `cv2=False` |
| Week07 | ROS2 + Qwen VLM | real reusable adapter、capacity-one latest-frame worker、semantic JSON compiled | Environment blocked | `rclpy=False`; no ROS2 camera/rosbag host or ML runtime |
| Week11 | LeRobotDataset | official metadata/dataset/sample API and CLI audited | Environment blocked | `lerobot=False`; dataset not downloaded |
| Week12 | SmolVLA inference | official `make_pre_post_processors → preprocess → select_action → postprocess` compiled and CLI audited | Environment blocked | `lerobot=False`, `torch=False`; no checkpoint/dataset runtime |
| Week13 | SmolVLA fine-tuning | official-style `lerobot-train` dry-run Executed; 20-step command generated; reload CLI compiled | Environment blocked | `lerobot-train` / CUDA unavailable; execute mode intentionally not run |
| Week14 | Isaac Sim observation | default scene and custom `--stage` paths compiled; launcher CLI audited | Environment blocked | `isaacsim=False`; only valid inside Isaac Sim 5.1 launcher |
| Week15 | Sim vs real observation | Basic domain/latency demos Executed; paired camera comparison documented | Environment blocked | `cv2=False` and no real camera input supplied |

No item is marked Network blocked, License blocked, or Model access blocked because downloads/authentication were not attempted after the local environment prerequisite check failed.

## API Sources Audited

- [Transformers LLaVA documentation](https://huggingface.co/docs/transformers/model_doc/llava)
- [Qwen2.5-VL model card](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)
- [LeRobot dataset loading example](https://github.com/huggingface/lerobot/blob/main/examples/dataset/load_lerobot_dataset.py)
- [LeRobot SmolVLA usage example](https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py)
- [LeRobot SmolVLA training documentation](https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx)
- [Isaac Sim quickstart](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim_robot.html)
- [Isaac Sim 5.1 Camera API](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/sensors/isaacsim_sensors_camera.html)

## Markdown Link Audit

- Markdown files scanned：354
- Missing active curriculum links：0
- Template-only unresolved examples：8，全部位於根目錄 `AGENTS.md` 的 weekly relative-link 範例，並非可點擊的實際 Week 文件。

## Conclusion

教材整合與 API-level correctness 已完成；大型模型、ROS2、LeRobot 與 Isaac Sim 的真實 runtime 尚未在本機環境執行，因此整體 `Runtime Validation` 只能標記為 `Partial`。
