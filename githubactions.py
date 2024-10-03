# Step 6: Create GitHub Actions Workflow (release-package.yml)
from audioop import add
import os

from git import Commit
import git
from httpcore import Origin

workflow_content = '''
name: Node.js Package

on:
  release:
    types: [created]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 16
      - run: npm ci
      - run: npm test

  publish-gpr:
    needs: build
    runs-on: ubuntu-latest
    permissions:
      packages: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 16
          registry-url: https://npm.pkg.github.com/
      - run: npm ci
      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{}}
'''

os.makedirs(".github/workflows", exist_ok=True)
with open(".github/workflows/release-package.yml", "w") as f:
    f.write(workflow_content)

print("GitHub Actions workflow created: release-package.yml")

# Step 7: Configure npm to Use GitHub Packages
npmrc_content = '''
@d347hm4n4g3r:registry=https://npm.pkg.github.com
'''

with open(".npmrc", "w") as f:
    f.write(npmrc_content)

print(".npmrc file created for GitHub Packages registry.")# Step 8: Final Commit and Push to GitHub
git add .github//workflows//release-package.yml .npmrc
git Commit -m "workflow to publish package"
git push Origin main # type: ignore
print("Workflow and .npmrc pushed to GitHub.")

