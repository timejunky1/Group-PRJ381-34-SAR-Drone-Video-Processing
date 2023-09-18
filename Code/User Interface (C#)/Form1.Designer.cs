namespace Infrared_Drone_Human_Detection_System
{
	partial class Form1
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
			this.btnUpload = new System.Windows.Forms.Button();
			this.btnDownload = new System.Windows.Forms.Button();
			this.btnExit = new System.Windows.Forms.Button();
			this.Video = new System.Windows.Forms.OpenFileDialog();
			this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
			this.lblProcessing = new System.Windows.Forms.Label();
			this.btnDownloadUM = new System.Windows.Forms.Button();
			this.label2 = new System.Windows.Forms.Label();
			this.label1 = new System.Windows.Forms.Label();
			this.pictureBox1 = new System.Windows.Forms.PictureBox();
			((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
			this.SuspendLayout();
			// 
			// btnUpload
			// 
			this.btnUpload.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(48)))), ((int)(((byte)(48)))), ((int)(((byte)(48)))));
			this.btnUpload.FlatAppearance.BorderColor = System.Drawing.Color.Black;
			this.btnUpload.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.btnUpload.ForeColor = System.Drawing.Color.White;
			this.btnUpload.Location = new System.Drawing.Point(469, 313);
			this.btnUpload.Name = "btnUpload";
			this.btnUpload.Size = new System.Drawing.Size(332, 85);
			this.btnUpload.TabIndex = 0;
			this.btnUpload.Text = "Upload Drone Video Footage";
			this.btnUpload.UseVisualStyleBackColor = false;
			this.btnUpload.Click += new System.EventHandler(this.btnUpload_Click);
			// 
			// btnDownload
			// 
			this.btnDownload.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(48)))), ((int)(((byte)(48)))), ((int)(((byte)(48)))));
			this.btnDownload.DialogResult = System.Windows.Forms.DialogResult.No;
			this.btnDownload.FlatAppearance.BorderColor = System.Drawing.Color.Black;
			this.btnDownload.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.btnDownload.ForeColor = System.Drawing.Color.White;
			this.btnDownload.Location = new System.Drawing.Point(52, 536);
			this.btnDownload.Name = "btnDownload";
			this.btnDownload.Size = new System.Drawing.Size(276, 50);
			this.btnDownload.TabIndex = 3;
			this.btnDownload.Text = "Download Documentation";
			this.btnDownload.UseVisualStyleBackColor = false;
			this.btnDownload.Click += new System.EventHandler(this.btnDownload_Click);
			// 
			// btnExit
			// 
			this.btnExit.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(48)))), ((int)(((byte)(48)))), ((int)(((byte)(48)))));
			this.btnExit.FlatAppearance.BorderColor = System.Drawing.Color.Black;
			this.btnExit.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.btnExit.ForeColor = System.Drawing.Color.White;
			this.btnExit.Location = new System.Drawing.Point(1011, 536);
			this.btnExit.Name = "btnExit";
			this.btnExit.Size = new System.Drawing.Size(163, 50);
			this.btnExit.TabIndex = 4;
			this.btnExit.Text = "Cancel";
			this.btnExit.UseVisualStyleBackColor = false;
			this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
			// 
			// Video
			// 
			this.Video.FileName = "Video";
			this.Video.FileOk += new System.ComponentModel.CancelEventHandler(this.Video_FileOk);
			// 
			// lblProcessing
			// 
			this.lblProcessing.Font = new System.Drawing.Font("Dubai", 7.875F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblProcessing.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(245)))), ((int)(((byte)(87)))), ((int)(((byte)(98)))));
			this.lblProcessing.Location = new System.Drawing.Point(258, 401);
			this.lblProcessing.Name = "lblProcessing";
			this.lblProcessing.Size = new System.Drawing.Size(754, 36);
			this.lblProcessing.TabIndex = 5;
			this.lblProcessing.Text = "Video processing...";
			this.lblProcessing.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			this.lblProcessing.Visible = false;
			this.lblProcessing.Click += new System.EventHandler(this.lblProcessing_Click);
			// 
			// btnDownloadUM
			// 
			this.btnDownloadUM.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(48)))), ((int)(((byte)(48)))), ((int)(((byte)(48)))));
			this.btnDownloadUM.FlatAppearance.BorderColor = System.Drawing.Color.Black;
			this.btnDownloadUM.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.btnDownloadUM.ForeColor = System.Drawing.Color.White;
			this.btnDownloadUM.Location = new System.Drawing.Point(498, 536);
			this.btnDownloadUM.Name = "btnDownloadUM";
			this.btnDownloadUM.Size = new System.Drawing.Size(276, 50);
			this.btnDownloadUM.TabIndex = 6;
			this.btnDownloadUM.Text = "Download User Manual";
			this.btnDownloadUM.UseVisualStyleBackColor = false;
			this.btnDownloadUM.Click += new System.EventHandler(this.btnDownloadUM_Click);
			// 
			// label2
			// 
			this.label2.Font = new System.Drawing.Font("Arial Rounded MT Bold", 13.875F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label2.ForeColor = System.Drawing.Color.White;
			this.label2.Location = new System.Drawing.Point(191, 49);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(989, 99);
			this.label2.TabIndex = 8;
			this.label2.Text = "Drone-Based AI Infrared Human Detection System for Disaster Response: A Proof-of-" +
    "Concept Simulation";
			this.label2.Click += new System.EventHandler(this.label2_Click);
			// 
			// label1
			// 
			this.label1.Font = new System.Drawing.Font("Arial Rounded MT Bold", 7.125F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label1.ForeColor = System.Drawing.Color.White;
			this.label1.Location = new System.Drawing.Point(111, 190);
			this.label1.Margin = new System.Windows.Forms.Padding(3);
			this.label1.Name = "label1";
			this.label1.Padding = new System.Windows.Forms.Padding(5);
			this.label1.Size = new System.Drawing.Size(1015, 102);
			this.label1.TabIndex = 7;
			this.label1.Text = resources.GetString("label1.Text");
			// 
			// pictureBox1
			// 
			this.pictureBox1.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("pictureBox1.BackgroundImage")));
			this.pictureBox1.ErrorImage = ((System.Drawing.Image)(resources.GetObject("pictureBox1.ErrorImage")));
			this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
			this.pictureBox1.InitialImage = ((System.Drawing.Image)(resources.GetObject("pictureBox1.InitialImage")));
			this.pictureBox1.Location = new System.Drawing.Point(55, 64);
			this.pictureBox1.Name = "pictureBox1";
			this.pictureBox1.Size = new System.Drawing.Size(130, 65);
			this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
			this.pictureBox1.TabIndex = 9;
			this.pictureBox1.TabStop = false;
			this.pictureBox1.Click += new System.EventHandler(this.pictureBox1_Click);
			// 
			// Form1
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoSize = true;
			this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(32)))), ((int)(((byte)(32)))), ((int)(((byte)(32)))));
			this.ClientSize = new System.Drawing.Size(1241, 620);
			this.Controls.Add(this.pictureBox1);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.btnDownloadUM);
			this.Controls.Add(this.btnExit);
			this.Controls.Add(this.btnDownload);
			this.Controls.Add(this.btnUpload);
			this.Controls.Add(this.lblProcessing);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "Form1";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "Infrared Human Detection System";
			this.Load += new System.EventHandler(this.Form1_Load);
			this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
			((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Label lblProcessing;
		private System.Windows.Forms.Button btnUpload;
		private System.Windows.Forms.Button btnDownload;
		private System.Windows.Forms.Button btnExit;
		private System.Windows.Forms.OpenFileDialog Video;
		private System.Windows.Forms.SaveFileDialog saveFileDialog1;
		private System.Windows.Forms.Button btnDownloadUM;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.PictureBox pictureBox1;
	}
}

