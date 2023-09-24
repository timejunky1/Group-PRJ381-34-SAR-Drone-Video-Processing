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
	public partial class Results : Form
	{
		public Results()
		{
			InitializeComponent();
            this.FormBorderStyle = FormBorderStyle.None;
        }

		private void btnExit_Click(object sender, EventArgs e)
		{
			Application.Exit();
		}

		private void pbMap_Click(object sender, EventArgs e)
		{
			try
			{
				SaveFileDialog saveFileDialog = new SaveFileDialog();
				saveFileDialog.Filter = "JPEG Image|*.jpg";
				saveFileDialog.Title = "Save Image As";
				saveFileDialog.FileName = "RescueMap.jpg";

				if (saveFileDialog.ShowDialog() == DialogResult.OK)
				{
					if (pbMap.Image != null)
					{
						// Use a temporary bitmap to save the image
						using (Bitmap tempBitmap = new Bitmap(pbMap.Image))
						{
							tempBitmap.Save(saveFileDialog.FileName, System.Drawing.Imaging.ImageFormat.Jpeg);
						}
						MessageBox.Show("Image saved successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
					}
					else
					{
						MessageBox.Show("Image is null.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
					}
				}
			}
			catch (Exception ex)
			{
				MessageBox.Show($"An error occurred: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}

		private void rtbOutput_TextChanged(object sender, EventArgs e)
		{

		}

		private void Results_Load(object sender, EventArgs e)
		{

		}

		private void Results_Paint(object sender, PaintEventArgs e)
		{
			Graphics g = e.Graphics;
			Pen myPen = new Pen(Color.FromArgb(61, 61, 61), 1);
			g.DrawLine(myPen, new Point(50, 110), new Point(800, 110));
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

		private void btnUploadAnother_Click(object sender, EventArgs e)
		{
			this.Close();
			Form1 form = new Form1();
			form.Show();
		}

		private void label2_Click(object sender, EventArgs e)
		{

		}
	}
}
