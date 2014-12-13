## Description

Semantic Versioning, or Semver as it's known on the streets, is an attempt to standardise the way that software versions are incrementally changed. In the world there are many different pieces of software whose developers have conflicting ideas about how software should be developed. For example, Dwarf Fortress is currently at version 0.40.13, whereas Google Chrome (which has been around for 2 years less than Dwarf Fortress) is currently at version 37.0.2062.124. How can those version numbers even be compared? They both represent around the same progress of development but in totally different ways. Semantic versioning aims to solve this problem by splitting the version string into 3, 4 or 5 parts:
<major>.<minor>.<patch>-<label>+<metadata>
major: Increased when your program changes in a way that makes it incompatible with older versions (major changes) - like the Python 2 to Python 3 change which, in order to make progress, broke a lot of existing programs.
minor: Increased when you add functionality but keep compatibility and don't change existing bits of the API (minor changes) - for example, adding a new section of a standard library to a programming language.
patch: Increased when you make minor functionality changes or bug fixes, like adding a new keyboard shortcut.
label: Used to indicate pre-release program status, such as beta, alpha or rc2 (release candidate 2.)
metadata: Used to describe build metadata when a version is in the early development stages - this might include the build date of the program.
For the purpose of this challenge, you will be sorting a list of Semantic Versions into chronological order, and you will do it like so:
First, compare the major version.
If they are the same, compare the minor version.
If they are the same, compare the patch version.
If those are all the same, check if the version has a label - ignore the content of the label. A version with a label (prerelease) comes before one without a label (final release.)
Ignore the build metadata.
If the semantic versions are still the same at this point, they can be considered the same version. For the purpose of this challenge we won't attempt to parse the label - but if you're feeling up to you can give it a try!
The full specification for Semantic Versioning can be found here.

### Input

You will first be given a number N. You will then be given N more lines, each one with a semantic version.

### Output

You will print the versions in chronological order, as described by the rules above.

