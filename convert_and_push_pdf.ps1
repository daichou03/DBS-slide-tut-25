$PPTXFolder = "week_1"
$PPTXFile = "week_1.pptx"
$PDFFile = "week_1.pdf"

# Get full paths
$PPTXPath = Join-Path $PPTXFolder $PPTXFile
$PDFPath = Join-Path $PPTXFolder $PDFFile

# Check if PowerPoint file exists
if (!(Test-Path $PPTXPath)) {
    Write-Host "Error: File $PPTXPath not found!"
    exit 1
}

# Convert PPTX to PDF using PowerPoint 365
Write-Host "🔄 Converting $PPTXFile to PDF..."
$PowerPoint = New-Object -ComObject PowerPoint.Application
$PowerPoint.Visible = $false
$Presentation = $PowerPoint.Presentations.Open((Get-Item $PPTXPath).FullName, $false, $false, $false)
$Presentation.SaveAs((Get-Item $PDFPath).FullName, 32)  # 32 = PDF format
$Presentation.Close()
$PowerPoint.Quit()
Write-Host "✅ Conversion completed: $PDFFile"

# Commit and push the updated PDF
Write-Host "📤 Pushing updated PDF to GitHub..."
git add $PDFPath
git commit -m "Automated PDF update"
git push origin main
Write-Host "✅ PDF pushed successfully!"
