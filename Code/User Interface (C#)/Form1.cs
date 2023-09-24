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
		Form2 setup = new Form2 ();

		public Form1()
		{
			InitializeComponent();
			this.FormBorderStyle = FormBorderStyle.None;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			setup.Hide();
		}

		private void btnUpload_Click(object sender, EventArgs e)
		{
			setup.Show();
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