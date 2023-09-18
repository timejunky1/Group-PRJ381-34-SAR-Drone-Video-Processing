using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Infrared_Drone_Human_Detection_System
{
	public partial class Form1 : Form
	{
		Results results = new Results();
		ScriptExecutioner se = new ScriptExecutioner();

		public Form1()
		{
			InitializeComponent();
			this.FormBorderStyle = FormBorderStyle.FixedSingle;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			results.Hide();
		}

		private void btnUpload_Click(object sender, EventArgs e)
		{
			Video.Title = "Select an MP4 Video File";
			//Filter for the OpenFileDialog to only allow .mp4 files
			Video.Filter = "MP4 files (*.mp4)|*.mp4";

			// Existing code for opening the file dialog
			if (Video.ShowDialog() == DialogResult.OK)
			{
				// Check if the selected file is an .mp4 file
				string videoFilePath = Video.FileName;
				string fileExtension = Path.GetExtension(videoFilePath);

				if (fileExtension.ToLower() != ".mp4")
				{
					MessageBox.Show("Please upload an MP4 file.", "Invalid File Type", MessageBoxButtons.OK, MessageBoxIcon.Error);
					return; // Exit early if the file is not an MP4
				}

				// Reset the label text and make it visible
				lblProcessing.Text = "Video processing...";
				lblProcessing.Visible = true;

				// Set the CONTEXT environment variable to 'APP'
				Environment.SetEnvironmentVariable("CONTEXT", "APP");

				// Refresh the form to reflect the label changes
				this.Refresh();

				// Existing code for running the Python script
				se.setpath("Human_Detection_Script.py");
				se.SetPerams(videoFilePath);
				string scriptOutput = se.ExecutePythonScript();

				// Check for any errors from the Python script
				if (!string.IsNullOrEmpty(scriptOutput))
				{
					lblProcessing.Text = "Error uploading video. Please try again and ensure the video is in the correct format.";
					MessageBox.Show(scriptOutput);
					return;  // Exit early if there's an error
				}

				// Existing code for retrieving output from the Python script
				string imageOutputPath = "humanMap.jpg";
				string textOutputPath = "locations.txt";

				if (File.Exists(imageOutputPath))
				{
					lblProcessing.Visible = false;
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
		}

		private void btnDownload_Click(object sender, EventArgs e)
		{
			saveFileDialog1.FileName = "Documentation.pdf";
			saveFileDialog1.Filter = "PDF files (*.pdf)|*.pdf";
			saveFileDialog1.DefaultExt = "pdf";
			saveFileDialog1.Title = "Choose a location to save the documentation";
			saveFileDialog1.OverwritePrompt = true;
			saveFileDialog1.CheckPathExists = true;

			// Show the save file dialog
			if (saveFileDialog1.ShowDialog() == DialogResult.OK)
			{
				string savePath = saveFileDialog1.FileName;

				try
				{
					// Specify the source path of the documentation file
					string sourcePath = Path.Combine(Application.StartupPath, "Documentation.pdf");

					// Copy the file to the chosen destination
					File.Copy(sourcePath, savePath, true); // Overwrite if exists

					MessageBox.Show("Documentation saved successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
				}
				catch (Exception ex)
				{
					MessageBox.Show($"An error occurred: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
				}
			}
		}

		private void btnExit_Click(object sender, EventArgs e)
		{
			Application.Exit();
		}

		private void label2_Click(object sender, EventArgs e)
		{

		}

		private void Form1_Load(object sender, EventArgs e)
		{

		}

		private void Form1_Paint(object sender, PaintEventArgs e)
		{
			Graphics g = e.Graphics;
			Pen myPen = new Pen(Color.FromArgb(61, 61, 61), 1); 
			g.DrawLine(myPen, new Point(50, 170), new Point(1200, 170));
		}

		private void btnDownloadUM_Click(object sender, EventArgs e)
		{
			saveFileDialog1.FileName = "User Manual.pdf";
			saveFileDialog1.Filter = "PDF files (*.pdf)|*.pdf";
			saveFileDialog1.DefaultExt = "pdf";
			saveFileDialog1.Title = "Choose a location to save the user manual";
			saveFileDialog1.OverwritePrompt = true;
			saveFileDialog1.CheckPathExists = true;

			// Show the save file dialog
			if (saveFileDialog1.ShowDialog() == DialogResult.OK)
			{
				string savePath = saveFileDialog1.FileName;

				try
				{
					// Specify the source path of the documentation file
					string sourcePath = Path.Combine(Application.StartupPath, "User Manual.pdf");

					// Copy the file to the chosen destination
					File.Copy(sourcePath, savePath, true); // Overwrite if exists

					MessageBox.Show("User Manual saved successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
				}
				catch (Exception ex)
				{
					MessageBox.Show($"An error occurred: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
				}
			}
		}

		private void pictureBox1_Click(object sender, EventArgs e)
		{

		}

		private void lblProcessing_Click(object sender, EventArgs e)
		{

		}

		private void Video_FileOk(object sender, CancelEventArgs e)
		{

		}
	}
}