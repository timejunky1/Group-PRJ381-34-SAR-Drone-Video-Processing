using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Infrared_Drone_Human_Detection_System
{
    internal class Perram
    {
        string videoType;
        float aspectRatio;
        int videoFrameCompretion;
        int frameSizeCompretion;
        public Perram(string videoType, float aspectRatio, int videoFrameCompretion, int frameSizeCompretion) 
        {
            this.videoFrameCompretion = videoFrameCompretion;
            this.videoType = videoType;
            this.frameSizeCompretion = frameSizeCompretion;
            this.aspectRatio = aspectRatio;
        }
    }
}
