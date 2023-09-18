namespace Infrared_Drone_Human_Detection_System
{
	partial class Results
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
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Results));
			this.pbMap = new System.Windows.Forms.PictureBox();
			this.rtbOutput = new System.Windows.Forms.RichTextBox();
			this.btnDownload = new System.Windows.Forms.Button();
			this.btnExit = new System.Windows.Forms.Button();
			this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
			this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
			this.label1 = new System.Windows.Forms.Label();
			this.btnUploadAnother = new System.Windows.Forms.Button();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			((System.ComponentModel.ISupportInitialize)(this.pbMap)).BeginInit();
			this.SuspendLayout();
			// 
			// pbMap
			// 
			this.pbMap.Location = new System.Drawing.Point(851, 73);
			this.pbMap.Margin = new System.Windows.Forms.Padding(0);
			this.pbMap.Name = "pbMap";
			this.pbMap.Size = new System.Drawing.Size(540, 706);
			this.pbMap.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
			this.pbMap.TabIndex = 2;
			this.pbMap.TabStop = false;
			this.pbMap.Click += new System.EventHandler(this.pbMap_Click);
			// 
			// rtbOutput
			// 
			this.rtbOutput.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(32)))), ((int)(((byte)(32)))), ((int)(((byte)(32)))));
			this.rtbOutput.ForeColor = System.Drawing.Color.White;
			this.rtbOutput.Location = new System.Drawing.Point(73, 207);
			this.rtbOutput.Name = "rtbOutput";
			this.rtbOutput.ReadOnly = true;
			this.rtbOutput.Size = new System.Drawing.Size(719, 391);
			this.rtbOutput.TabIndex = 8;
			this.rtbOutput.Text = "";
			this.rtbOutput.TextChanged += new System.EventHandler(this.rtbOutput_TextChanged);
			// 
			// btnDownload
			// 
			this.btnDownload.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(48)))), ((int)(((byte)(48)))), ((int)(((byte)(48)))));
			this.btnDownload.FlatAppearance.BorderColor = System.Drawing.Color.Black;
			this.btnDownload.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.btnDownload.ForeColor = System.Drawing.Color.White;
			this.btnDownload.Location = new System.Drawing.Point(22, 715);
			this.btnDownload.Name = "btnDownload";
			this.btnDownload.Size = new System.Drawing.Size(276, 50);
			this.btnDownload.TabIndex = 9;
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
			this.btnExit.Location = new System.Drawing.Point(647, 715);
			this.btnExit.Name = "btnExit";
			this.btnExit.Size = new System.Drawing.Size(163, 50);
			this.btnExit.TabIndex = 10;
			this.btnExit.Text = "Cancel";
			this.btnExit.UseVisualStyleBackColor = false;
			this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
			// 
			// openFileDialog1
			// 
			this.openFileDialog1.FileName = "openFileDialog1";
			// 
			// label1
			// 
			this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
			this.label1.AutoSize = true;
			this.label1.Font = new System.Drawing.Font("Arial Rounded MT Bold", 13.875F);
			this.label1.ForeColor = System.Drawing.Color.White;
			this.label1.Location = new System.Drawing.Point(208, 51);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(471, 43);
			this.label1.TabIndex = 11;
			this.label1.Text = "Human Detection Results";
			// 
			// btnUploadAnother
			// 
			this.btnUploadAnother.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(48)))), ((int)(((byte)(48)))), ((int)(((byte)(48)))));
			this.btnUploadAnother.FlatAppearance.BorderColor = System.Drawing.Color.Black;
			this.btnUploadAnother.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.btnUploadAnother.ForeColor = System.Drawing.Color.White;
			this.btnUploadAnother.Location = new System.Drawing.Point(334, 715);
			this.btnUploadAnother.Name = "btnUploadAnother";
			this.btnUploadAnother.Size = new System.Drawing.Size(276, 50);
			this.btnUploadAnother.TabIndex = 12;
			this.btnUploadAnother.Text = "Upload Another Video";
			this.btnUploadAnother.UseVisualStyleBackColor = false;
			this.btnUploadAnother.Click += new System.EventHandler(this.btnUploadAnother_Click);
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label2.ForeColor = System.Drawing.Color.White;
			this.label2.Location = new System.Drawing.Point(891, 44);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(443, 29);
			this.label2.TabIndex = 13;
			this.label2.Text = "Reconstructed Map of Disaster Zone:";
			this.label2.Click += new System.EventHandler(this.label2_Click);
			// 
			// label3
			// 
			this.label3.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
			this.label3.AutoSize = true;
			this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label3.ForeColor = System.Drawing.Color.White;
			this.label3.Location = new System.Drawing.Point(136, 158);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(615, 29);
			this.label3.TabIndex = 14;
			this.label3.Text = "Location Information of Possible Victims in Distress:";
			// 
			// label4
			// 
			this.label4.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
			this.label4.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(245)))), ((int)(((byte)(87)))), ((int)(((byte)(98)))));
			this.label4.Location = new System.Drawing.Point(68, 616);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(756, 50);
			this.label4.TabIndex = 15;
			this.label4.Text = "Please note: For simulation purposes, the pixel coordinates represent GPS coordin" +
    "ates in a real life scenario.";
			// 
			// Results
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoSize = true;
			this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(32)))), ((int)(((byte)(32)))), ((int)(((byte)(32)))));
			this.ClientSize = new System.Drawing.Size(1429, 808);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.btnUploadAnother);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.btnExit);
			this.Controls.Add(this.btnDownload);
			this.Controls.Add(this.rtbOutput);
			this.Controls.Add(this.pbMap);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "Results";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "Infrared Human Detection System";
			this.Load += new System.EventHandler(this.Results_Load);
			this.Paint += new System.Windows.Forms.PaintEventHandler(this.Results_Paint);
			((System.ComponentModel.ISupportInitialize)(this.pbMap)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		public System.Windows.Forms.PictureBox pbMap;
		public System.Windows.Forms.RichTextBox rtbOutput;
		private System.Windows.Forms.Button btnDownload;
		private System.Windows.Forms.Button btnExit;
		private System.Windows.Forms.OpenFileDialog openFileDialog1;
		private System.Windows.Forms.SaveFileDialog saveFileDialog1;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Button btnUploadAnother;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.Label label4;
	}
}