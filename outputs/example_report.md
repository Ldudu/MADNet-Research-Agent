# MADNet Research Agent Report

## Question
What are the open issues in remote sensing VSR?

## Planner Output
- Sub-goals: identify dominant modeling themes, compare evaluation and dataset assumptions, surface unresolved limitations and open issues
- Focus dimensions: method, degradation, dataset, metric, limitation

## Analyst Findings
- Open problems in remote sensing video super-resolution: Summarizes unresolved challenges across degradation realism, alignment robustness, and benchmark design.
- Benchmarking remote sensing VSR evaluation protocols: Compares evaluation setups across satellite and aerial video benchmarks.
- Motion-aware degradation modeling for remote sensing VSR: Jointly models blur, aliasing, jitter, and compression instead of assuming clean bicubic downsampling.
- Temporal alignment under satellite viewpoint drift: Studies temporal alignment failure when camera motion and target motion coexist.
- Most evidence emphasizes degradation realism, temporal alignment, and benchmark comparability as central research bottlenecks.

## Evidence Table
| Evidence | Datasets | Metrics | Noted Limitation |
| --- | --- | --- | --- |
| Open problems in remote sensing video super-resolution | RS-VSRBench, FlightSet-Real | PSNR, SSIM, Perceptual Quality | The survey highlights problems but does not propose a unified solution. |
| Benchmarking remote sensing VSR evaluation protocols | GeoVideo-Sim, AeroTrack-32, RS-VSRBench | PSNR, SSIM, LPIPS, NIQE | Benchmark coverage is still narrow for cloud, haze, and low-light conditions. |
| Motion-aware degradation modeling for remote sensing VSR | Synthetic-SatVSR, OrbitClip-24 | PSNR, SSIM, LPIPS | The degradation recipe is still synthetic, so real-world transfer remains weak. |
| Temporal alignment under satellite viewpoint drift | OrbitClip-24, GeoVideo-Sim | PSNR, tOF, Warp Error | Performance drops on long clips with abrupt scene change. |

## Critic Review
- Evidence covers the major themes, but unified evaluation protocols and real-world validation remain incomplete.

## Risks
- The sample corpus is illustrative and should be replaced with real paper notes for production use.
- A high-level synthesis can still overfit to the retrieved shortlist if recall is poor.

## Conclusion
The current evidence suggests that remote sensing VSR still faces three recurring barriers: realistic degradation modeling, robust temporal alignment under viewpoint drift, and fair benchmark design. A useful next step is to connect this workflow to a larger literature corpus and a real LLM-backed extractor.
