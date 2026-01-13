# PowerShell script to create GitHub repository using GitHub API
# Usage: .\create_repo.ps1 -Token "YOUR_GITHUB_TOKEN" -RepoName "tts-app"

param(
    [Parameter(Mandatory=$true)]
    [string]$Token,
    
    [Parameter(Mandatory=$false)]
    [string]$RepoName = "tts-app"
)

$headers = @{
    "Authorization" = "token $Token"
    "Accept" = "application/vnd.github.v3+json"
}

$body = @{
    name = $RepoName
    description = "Text-to-Speech application with CLI and Streamlit web app"
    private = $false
} | ConvertTo-Json

$uri = "https://api.github.com/user/repos"

try {
    Write-Host "Creating repository '$RepoName' on GitHub..." -ForegroundColor Yellow
    $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body -ContentType "application/json"
    
    Write-Host "✅ Repository created successfully!" -ForegroundColor Green
    Write-Host "Repository URL: $($response.html_url)" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Now I'll push your code to this repository..." -ForegroundColor Yellow
    
    # Add remote and push
    cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"
    git remote remove origin 2>$null
    git remote add origin "https://github.com/yeswanthsetti-tech/$RepoName.git"
    git branch -M main
    
    Write-Host "Pushing code to GitHub..." -ForegroundColor Yellow
    git push -u origin main
    
    Write-Host ""
    Write-Host "✅ SUCCESS! Your code is now on GitHub!" -ForegroundColor Green
    Write-Host "Repository: $($response.html_url)" -ForegroundColor Cyan
    
} catch {
    Write-Host "❌ Error: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $responseBody = $reader.ReadToEnd()
        Write-Host "Response: $responseBody" -ForegroundColor Red
    }
    exit 1
}
