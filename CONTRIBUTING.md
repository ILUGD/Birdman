# Contributions Best Practices

This document shall give you an overview of how you can contribute to the project.
It is split up in these parts:

- [Ways to go for your contribution][how-to-contribute]
- [General Practices to keep in mind when contributing][general-practices]

## How To Contribute
[how-to-contribute]: #how-to-contribute

This section includes a collection of ways to contribute.
The purpose of the different issue templates is to guide contributors and to allow synchronization with other developers.

### Report A Bug

Please see if the bug was reported before by searching the [issue tracker][issues] for some key words you would say.
In case it was, you can collaborate, leave a comment and get into discussion.

To report a bug, please open a new issue following [this issue template]().
A bug might be unexpected behavior or a clear violation of design principles.

### Request a Feature

Please see if the feature was reported before by searching the [issue tracker][issues] for some key words you would say.
In case it was, you can collaborate, leave a comment and get into discussion.

If you have a new idea about how to improve Birdman, please open an issue for your feature request.

### Solve an Issue
.
You can choose to comment on an issue that you like to work on it.
Please share your progress as soon as possible by creating a pull request.
You do not have to ask for permission to solve an issue.
You can just do it.
To reduce duplicated work however, please coordinate in the issue with other people.
If you do not get a response, feel free to solve the issue yourself.

### Create First-Timer Issues

In case the issue is easy and you are an advanced programmer, you can use the issue to
guide new contributors by choosing not to solve it but telling that you like to help out and
giving hints for a solution.

You can use the issue template with the label good first issue
to indicate that this issue is suitable for beginners.
Also, please describe in the issue what steps are to be taken to solve it (Implementation Plan) and what a solution looks like (Closing Criteria).

### Fix a Bug

If you like to help improve the App or a bug caught your eye and you like to fix it:

1. Leave a comment that you like to work on it.
2. See if someone else opened a pull request. If so, you can choose to comment that you like to cooperate.
3. If there is no pull request by other people within a day, feel free to create your own pull request within one day.

### Create a Pull Request
[create-pr]: #create-a-pull-request

If you create a pull request, you do not need to solve all problems at once.
We like little steps more because they are easier to understand.
Please follow the pull request template or change it.

To inform other people about your work and to enable them to use our work,
consider to create pull requests as soon as possible, after the first small commit.

### Document How to Contribute

Contribution is made easy through well documented APIs.
You can find documentation on how to contribute here:
- [CONTRIBUTING.md](CONTRIBUTING.md) summarizes ways to contribute and motivates them
- [README.md](README.md) includes documentation on how to go about contributions. A README.md is present in all directories

  

Please open an issue to let us know where to improve the documentation.

### Add New Ways to Contribute

You can add new of these entries to this section.
Please evaluate your idea like this:
- If it can be done once and is completed, it is an issue, not a task.
- If it can be done endlessly and is done once, it is a task.
- If you mix both in a task, think about adding a task enablement issue.

Then, open a new issue.

You can cooperate on pull requests with other contributors.
You can use techniques like [pair programming](https://www.youtube.com/watch?v=vgkahOzFH2Q) or
collaborate together on branches of your forks.
You can attribute a pull-request also to other people who helped you out or submit a pull-request
where you and an other person contributed together.

You can comment on an existing [issue][issues] that you like to cooperate with specific people or
ask in the [chat] if anyone would be interested in cooperating.

### Improve the Code Quality

Improving the code quality makes it easier to add new code which is flawless.
This is also a traning for you to write good code and to make a meaningful
contribution to existing code while learning it.

If you like to improve the code, please [open an issue][issue-code-quality] to let us know what you are working on and coordinate the effort.



[pr-template]:                  .github/PULL_REQUEST_TEMPLATE.md
[new-pr]:                       https://github.com/ILUGD/Birdman/pulls/new
[issues]:                       https://github.com/ILUGD/Birdman/issues
[chat]:                         https://t.me/joinchat/EQLMk0li-obJcUsX69bGIg


## General Contribution Practices
[general-practices]: #general-contribution-practices

### Commits
* Write clear meaningful git commit messages (Do read http://chris.beams.io/posts/git-commit/)
* Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (More info at https://github.com/blog/1506-closing-issues-via-pull-requests )
* When you make very very minor changes to a PR of yours (like for example fixing a failing travis build or some small style corrections or minor changes requested by reviewers) make sure you squash your commits afterwards so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at https://davidwalsh.name/squash-commits-git )


### Feature Requests and Bug Reports
* When you file a feature request or when you are submitting a bug report to the [issue tracker][issues], make sure you add steps to reproduce it. Especially if that bug is some weird/rare one.
* Please have a look if someone else suggested something similar and see it a new issue is necessary.
* Please follow the issue template.

### Join the development
* Before you join development, please set up the project on your local machine, run it and go through the application completely.
* If you would like to work on an issue, drop in a comment at the issue. If it is already assigned to someone, but there is no sign of any work being done, please free to drop in a comment so that the issue can be assigned to you if the previous assignee has dropped it entirely.


### Licensing Code
We recommend you add code and work which you did yourself. By adding this code to the repository, you put it under the [GNU LICENSE](LICENSE).  
If you embed other work, you need to be compatible with the current license. Licenses compatible are e.g. MIT, GPL, AGPL, LGPL, BSD. **In almost no case is it legal to just copy the code/files without license.**
- [Embedding MIT](https://opensource.stackexchange.com/questions/6342/where-to-put-license-for-mit-licensed-code-on-website): You need to keep the license close to the code:
  - CSS/HTML/Javascript: embed it into the code, it is not that long
  - binary files e.g. fonts: create a file with the same name next to the binary file with `.license` in the end and copy the license in there.
- Stackoverflow: Link to the answer or question.
- ... append in the future.
