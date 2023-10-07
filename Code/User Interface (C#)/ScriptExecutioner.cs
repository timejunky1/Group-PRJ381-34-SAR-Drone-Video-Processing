using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Infrared_Drone_Human_Detection_System
{
    internal class ScriptExecutioner
    {
        string pathToScript;
        string arguments;

        public void setpath(string pathToScript)
        {
            this.pathToScript = pathToScript;
            this.arguments = $"external";
        }

        public void SetPerams(string vfp, bool useModel)
        {
            arguments = $"\"{vfp},{useModel}\" external";
        }

        public string ExecutePythonScript()
        {
            try
            {
                StringBuilder output = new StringBuilder();
                StringBuilder errors = new StringBuilder();

                string userProfile = Environment.GetEnvironmentVariable("USERPROFILE");
                string pythonPath = $@"{userProfile}\AppData\Local\Programs\Python\Python311\python.exe";

                ProcessStartInfo start = new ProcessStartInfo
                {
                    FileName = pythonPath,
                    Arguments = $"{pathToScript} {arguments}",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    CreateNoWindow = true
                };

                using (Process process = new Process { StartInfo = start })
                {
                    process.OutputDataReceived += (sender, e) =>
                    {
                        if (e.Data != null)
                        {
                            output.AppendLine(e.Data);
                        }
                    };

                    process.ErrorDataReceived += (sender, e) =>
                    {
                        if (e.Data != null)
                        {
                            errors.AppendLine(e.Data);
                        }
                    };

                    process.Start();
                    process.BeginOutputReadLine();
                    process.BeginErrorReadLine();
                    process.WaitForExit();

                    if (errors.Length > 0)
                    {
                        return errors.ToString();
                    }

                    return output.ToString();
                }
            }
            catch (Exception ex)
            {
                return ex.Message;
            }
        }
    }
}
