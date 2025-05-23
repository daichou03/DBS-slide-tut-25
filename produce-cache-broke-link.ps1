# Define repository and branch information
$repoOwner = "daichou03"
$repoName = "DBS-slide-tut-25"
$branch = "main"

# Prompt for file path (with default)
$filePath = Read-Host "Enter file path (default: week_1/week_1.pptx)"
if ([string]::IsNullOrWhiteSpace($filePath)) {
    $filePath = "week_1/week_1.pptx"
}

# Construct API URL for commit history of the file
$apiUrl = "https://api.github.com/repos/${repoOwner}/${repoName}/commits?path=${filePath}"

# Call GitHub API (User-Agent header is required)
try {
    $commits = Invoke-RestMethod -Uri $apiUrl -Headers @{ "User-Agent" = "PowerShell" }
} catch {
    Write-Error "Failed to retrieve commit data. Ensure the file path is correct and you have internet access."
    exit
}

if (-not $commits) {
    Write-Error "No commit data found for the specified file."
    exit
}

# Get the commit date from the most recent commit
$lastUpdated = $commits[0].commit.committer.date
Write-Output "Last commit date (UTC): $lastUpdated"

# Convert the date to a Unix timestamp
$date = [datetime]::Parse($lastUpdated)
$unixTimestamp = [int](([datetimeOffset]$date).ToUnixTimeSeconds())

# Construct the raw URL with the cache-busting token in the new format
$rawUrl = "https://github.com/${repoOwner}/${repoName}/raw/refs/heads/${branch}/${filePath}?token=${unixTimestamp}"

Write-Output "`nRaw URL with cache busting token:"
Write-Output $rawUrl
