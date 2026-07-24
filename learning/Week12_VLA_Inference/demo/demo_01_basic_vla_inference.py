"""CPU/GPU 可控的 VLA 介面 Basic Demo；使用 deterministic mock policy。"""
import argparse,time
import numpy as np
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--device",choices=["cpu","gpu"],default="cpu");p.add_argument("--chunk",type=int,default=4);a=p.parse_args()
    if a.chunk<=0:p.error("--chunk 必須正整數")
    if a.device=="gpu":
        print("GPU mode requested; Basic Demo 仍使用 NumPy，真實 GPU 模型需另行安裝。")
    state=np.array([.1,-.2,.3],dtype=np.float32)
    start=time.perf_counter();actions=np.tile(-.1*state,(a.chunk,1));elapsed=time.perf_counter()-start
    print(f"observation_state_shape={state.shape}")
    print(f"predicted_action_chunk_shape={actions.shape}")
    print(actions)
    print(f"basic_interface_latency_ms={elapsed*1000:.3f} (not a model benchmark)")
if __name__=="__main__":main()
