using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Infrared_Drone_Human_Detection_System
{
    public partial class Form2 : Form
    {
        Results results = new Results();
        ScriptExecutioner se = new ScriptExecutioner();
        string videoFilePath;
        string fileExtension;
        bool ready;
        string direction = "(0,0)";
        bool useModel = false;

        public Form2()
        {
            InitializeComponent();
            this.FormBorderStyle = FormBorderStyle.None;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            results.Hide();
            desclabel.Visible = false;
            comboBox1.DataSource = new List<string>() { "Demo With Auto Piloting", "Demo with manual piloting" };
            ready = false;
            lblProcessing.Visible = false;
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void Form2_Load(object sender, EventArgs e)
        {
            
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Video.Title = "Select an MP4 Video File";
            //Filter for the OpenFileDialog to only allow .mp4 files
            Video.Filter = "MP4 files (*.mp4)|*.mp4";

            // Existing code for opening the file dialog
            if (Video.ShowDialog() == DialogResult.OK)
            {
                // Check if the selected file is an .mp4 file
                videoFilePath = Video.FileName;
                fileExtension = Path.GetExtension(videoFilePath);
                lblVideo.ForeColor = Color.Green;
                lblVideo.Text = ".." + videoFilePath.Substring(videoFilePath.IndexOf(".mp4") - 20);
                ready= true;

                if (fileExtension.ToLower() != ".mp4")
                {
                    MessageBox.Show("Please upload an MP4 file.", "Invalid File Type", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    lblVideo.ForeColor = Color.Red;
                    ready = false;
                    return; // Exit early if the file is not an MP4
                }

            }   
        }

        private void label1_MouseHover(object sender, EventArgs e)
        {
            desclabel.Visible = true;
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }

        private void btnProcess_Click(object sender, EventArgs e)
        {
            
            if(!ready) 
            {
                MessageBox.Show("Make sure the settings are correct");
                return; 
            };

            btnProcess.Enabled = false;
            btnProcess.Visible = false;
            comboBox1.Enabled= false;
            rbUseModel.Enabled= false;
            btnAdd.Enabled= false;
            btnRemove.Enabled= false;
            button1.Enabled= false;
            lblProcessing.Visible = true;

            useModel = rbUseModel.Checked;
            string peramsOutputPath = "directions.txt";
            if (File.Exists(peramsOutputPath))
            {
                File.Delete(peramsOutputPath);
            }
            using (FileStream stream = new FileStream(peramsOutputPath, FileMode.Create))
            {
                using (StreamWriter sw = new StreamWriter(stream))
                {
                    foreach(string li in listBox1.Items)
                    {
                        sw.WriteLine(li.ToString());
                    }
                }
            }

            // Set the CONTEXT environment variable to 'APP'
            Environment.SetEnvironmentVariable("CONTEXT", "APP");

            // Refresh the form to reflect the label changes
            this.Refresh();

            // Existing code for running the Python script
            se.SetPerams(videoFilePath, useModel);
            string scriptOutput = se.ExecutePythonScript();

            // Check for any errors from the Python script
            if (!string.IsNullOrEmpty(scriptOutput))
            {
                //lblProcessing.Text = "Error uploading video. Please try again and ensure the video is in the correct format.";
                MessageBox.Show(scriptOutput);
                return;  // Exit early if there's an error
            }
            MessageBox.Show(scriptOutput);

            // Existing code for retrieving output from the Python script

            string imageOutputPath = "humanMap.jpg";
            string textOutputPath = "locations.txt";

            if (File.Exists(imageOutputPath))
            {
                //lblProcessing.Visible = false;
                this.Hide();
                results.Show();

                using (FileStream stream = new FileStream(imageOutputPath, FileMode.Open))
                {
                    results.pbMap.Image = new Bitmap(stream);
                }

                // Delete the image file after processing
                File.Delete(imageOutputPath);
            }

            if (File.Exists(textOutputPath))
            {
                this.Hide();
                results.Show();

                if (File.ReadAllText(textOutputPath) == "")
                {
                    results.rtbOutput.Text = "No humans detected on map.";
                }
                else
                {
                    results.rtbOutput.Text = File.ReadAllText(textOutputPath);
                }

                // Delete the text file after processing
                File.Delete(textOutputPath);
            }
            else
            {
                MessageBox.Show("Text file not found.");
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox1.SelectedIndex == 0)
            {
                se.setpath("Human_Detection_Script.py");
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                se.setpath("Human_Detection_Alternative.py");
            }
        }

        private void label1_MouseLeave(object sender, EventArgs e)
        {
            desclabel.Visible = false;
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            string previousDirection = "(0,0)";
            int lastIndex = listBox1.SelectedIndex;
            if (lastIndex == -1)
            {
                if(listBox1.Items.Count > 0)
                {
                    lastIndex = listBox1.Items.Count - 1;
                }
                else
                {
                    lastIndex = 0;
                }
            }
            if(lastIndex > 0)
            {
                previousDirection = listBox1.Items[lastIndex-1].ToString();
            }


            if ((left.Checked || forward.Checked || right.Checked || back.Checked) && direction != previousDirection)
            {
                listBox1.Items.Insert(lastIndex, direction);
            }
            else 
            {
                lblDirection.ForeColor= Color.Red;
                lblDirection.Text = "?";
            }
        }

        private void btnRemove_Click(object sender, EventArgs e)
        {
            listBox1.Items.RemoveAt(listBox1.SelectedIndex);
        }

        private void forward_CheckedChanged(object sender, EventArgs e)
        {
            lblDirection.ForeColor = Color.Green;
            direction = "(0,1)";
            lblDirection.Text = direction;
        }

        private void right_CheckedChanged(object sender, EventArgs e)
        {
            lblDirection.ForeColor = Color.Green;
            direction = "(1,0)";
            lblDirection.Text = direction;
        }

        private void back_CheckedChanged(object sender, EventArgs e)
        {
            lblDirection.ForeColor = Color.Green;
            direction = "(0,-1)";
            lblDirection.Text = direction;
        }

        private void left_CheckedChanged(object sender, EventArgs e)
        {
            lblDirection.ForeColor = Color.Green;
            direction = "(-1,0)";
            lblDirection.Text = direction;
        }
    }
}
