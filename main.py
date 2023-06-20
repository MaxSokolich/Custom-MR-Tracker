
from Tracking.Custom2DTracker import Tracker
from Params import CONTROL_PARAMS,CAMERA_PARAMS,STATUS_PARAMS
from Tracking.AnalysisClass import Analysis

if __name__ == "__main__":
    
    tracker = Tracker(CONTROL_PARAMS,CAMERA_PARAMS,STATUS_PARAMS)
        #self.tracker = tracker

    video_name = "/Users/bizzarohd/Desktop/spinningmanipulation2.mov"

    output_name = "test"
    
    

    robot_list = tracker.main(video_name,output_name)

    analysis = Analysis(CONTROL_PARAMS,CAMERA_PARAMS,STATUS_PARAMS,robot_list)
    analysis.convert2pickle(output_name)
    try:
        analysis.plot()
    except Exception:
        pass