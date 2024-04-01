# ONNX Runtime - Object detection with YOLO

Check [this guide](https://www.pipeless.ai/docs/v1/examples/onnx-yolo) to run the example step by step.


```json
{
    "runtime": "onnx",
    "model_uri": "https://pipeless-public.s3.eu-west-3.amazonaws.com/yolov8n.onnx",
    "inference_params": {
        "execution_provider": "cpu"
    }
}
```