# Security Vulnerabilities Reporting

## Learning goals

Thourgh this group work, you will learn how to read code, search and report security vulnarabilities.  You can also try to fix some of them. 🚀

## Backgroud 

You are given is a tiny program (see main.py) with-text based user inteface, which allows one the store basic information on students.  There are many serious  flaws and vulnarabilities in the program. You will practice finding, reporting and  and fixing them.  Please read more background information (including assessment criteria) in Canvas.

## Preparatory actions

1. Creare a new repository for your team based on this templete called "faultystudentrecord".  See instructions at [GitHub Docs: Creating a repository from a template] (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
2. Enable security  vulnerabilities reporting for your repository. See instructions at  [GitHub Docs: Configuring private vulnerability reporting for a repository] (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository)
3. Protect the main branch of your repository.  Notice a blue warning message about an unprotected branch and follow a link to the branch protection settings.  Under "Protect matching branches", select "Require a pull request before merging". Optionally, to require approval (by another group member) before a pull request can be merged, you can also select "Require approvals". See more instructions at [GitHub Docs: Managing a branch protection rule] https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule

## Workflow actions

1.  Examine the main code (main.py) carefully and test different usage scenarous.  You can test code either manually (this is, by running the code and entering values by hand) or code automatic tests.  You can find examples of simple hardcoded unit tests in test.py (please note that harcoding unit tests is not good practice in most professional contexts, but works well for this exercise) and expand on those.
2.  For finding issues that are more difficult to spot, search online for information about  "SQL injection" and "Directory Traversal".  
3.  As soon as you find a security flaw, use GitHub to file a Security Vulnarability Report. Use this template as a basis of your vulnability report: [Vulnerability Report Templete by GitHub Security Lab] (https://github.com/github/securitylab/blob/main/docs/report-template.md).  The text-based report does not have mandatory fields, but you should provide as much information as possible.  It is particularly important to provide exact steps to reproduce the vulnerablity (in this case,  tested example code on how an attacker could use it).  There must be a seperate report for each vulnerability found.
4. If you still have time, try fixing some of the found security  vulnerabilities (or make other well-reasoned improvements to the code).  Please edit the code with Visual Studio Code and, preferably, also try out GitHop Copilot extension (btw, this can also help spot new security flaws). Please always make your code changes first to a new branch, then send pull request to the main repository and merge the repositories.
5. Make sure that all relevant code changes are merged into the main repository before submitting the assigment for review. See Canvas for instructions on how to submit. 
    

