# SoccerNet - Tracking

Welcome to the SoccerNet Development Kit for the Tracking Task and Challenge. This kit is meant as a help to get started working with the data and the proposed task. More information about the dataset can be found on our [official website](https://soccer-net.org/).

<p align="center"><img src="Images/GraphicalAbstract-tracking.png" width="640"></p>

The Tracking dataset consists of 12 complete soccer games from the main camera including:
 - 200 clips of 30 seconds with tracking data.
 - one complete halftime annotated with tracking data.
 - the complete videos for the 12 games.

Participate in our upcoming Challenge at CVPR and try to win up to 1000$ sponsored by [Baidu](https://www.baidu.com/)! All details can be found on the [challenge website](https://eval.ai/web/challenges/challenge-page/761/overview), or on the [main page](https://soccer-net.org/).

The participation deadline is fixed at the 30th of May 2022.
The official rules and guidelines are available on [ChallengeRules.md](ChallengeRules.md).

## How to download SoccerNet-tracking

A [SoccerNet pip package](https://pypi.org/project/SoccerNet/) to easily download the data and the annotations is available. 

To install the pip package simply run:

<code>pip install SoccerNet</code>

```python
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="path/to/SoccerNet")
mySoccerNetDownloader.downloadGames(files=["SocccerNet-MOT.zip"], task="tracking") # download frames and labels for the 150 clips of the challenge - Requires around 30 GB of local storage
```

Please follow the instructions provided in the [Download](Download) folder of this repository. Do also mind that signing an Non-Disclosure agreement (NDA) is required to access the LQ and HQ videos: [NDA](https://docs.google.com/forms/d/e/1FAIpQLSfYFqjZNm4IgwGnyJXDPk2Ko_lZcbVtYX73w5lf6din5nxfmA/viewform).

## Benchmark Implementations

This repository contains several [benchmarks](Benchmarks) for action spotting. You can use these codes to build upon our methods and improve the performances.

## Evaluation

[TBD] Check out the MOT20 Evaluation Kit.

## Visualizations

[TBD] Check out the MOT20 Evaluation Kit.

## Citation

For further information check out the paper and supplementary material:

Please cite our work if you use our dataset:
```bibtex
@InProceedings{Deliège2020SoccerNetv2,
      title={SoccerNet-tracking}, 
      author={},
      year={2022},
      booktitle = {},
      month = {},
}
```
