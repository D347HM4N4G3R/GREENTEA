# Step 8: Final Commit and Push to GitHub
!git add .github/workflows/release-package.yml .npmrc
!git commit -m "workflow to publish package"
!git push origin main
print("Workflow and .npmrc pushed to GitHub.")