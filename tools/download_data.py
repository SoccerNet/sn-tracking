from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="./")
mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train","test","challenge"])