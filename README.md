# SoccerNet - Tracking

Welcome to the SoccerNet Development Kit for the Tracking Task and Challenge. This kit is meant as a help to get started working with the data and the proposed task. More information about the dataset can be found on our [official website](https://www.soccer-net.org/).

<p align="center"><img src="Images/GraphicalAbstract-tracking.png" width="640"></p>

The Tracking dataset consists of 12 complete soccer games from the main camera including:
 - 200 clips of 30 seconds with tracking data.
 - one complete halftime annotated with tracking data.
 - the complete videos for the 12 games.

Note that a subset of this data is used in this first challenge. (150 clips of 30 seconds)

Participate in our upcoming Challenge at CVPR and try to win up to 1000$ sponsored by [Baidu](https://www.baidu.com/)! All details will soon be available on the [challenge website](https://eval.ai/web/challenges/challenge-page/761/overview), or on the [main page](https://www.soccer-net.org/).

The participation deadline is fixed at the 30th of May 2022.
The official rules and guidelines will be provided in [ChallengeRules.md](ChallengeRules.md) around mid-February 2022.

<a href="https://youtu.be/tA9E1hkiyB0">
<p align="center"><img src="Images/Thumbnail.png" width="720"></p>
</a>

## How to download SoccerNet-tracking

The data for the train and test sets will be available at the beginning of March 2022 and the challenge set around mid-March.

<!--
A [SoccerNet pip package](https://pypi.org/project/SoccerNet/) to easily download the data and the annotations is available. 

To install the pip package simply run:

<code>pip install SoccerNet</code>

```python
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="path/to/SoccerNet")
mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train","valid","test","challenge"]) # download all splits for the tracking task - Requires around 30 GB of local storage
```

-->
## Benchmark Implementations

This repository will soon contain several [benchmarks](Benchmarks) for the tracking task. You can use these codes to build upon our methods and improve the performances.

## Evaluation

We use the [TrackEval](https://github.com/JonathonLuiten/TrackEval) repository to evaluate the performances. More details will come soon.

## Visualizations

You can use the [MOT Challenge Evaluation Kit](https://github.com/dendorferpatrick/MOTChallengeEvalKit) to visualize the tracks.

## Our other Challenges

Check out our other challenges related to SoccerNet!
- [Action Spotting](https://github.com/SoccerNet/sn-spotting)
- [Replay Grounding](https://github.com/SoccerNet/sn-grounding)
- [Calibration](https://github.com/SoccerNet/sn-calibration)
- [Re-Identification](https://github.com/SoccerNet/sn-reid)
- [Tracking](https://github.com/SoccerNet/sn-tracking)

## Citation

For further information check out the paper and supplementary material:

Please cite our work if you use our dataset:
```bibtex
Available soon
```
