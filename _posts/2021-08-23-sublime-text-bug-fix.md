---
layout: post
title: Fixing Sublime Text's SideBarEnhancements Plugin
categories: [Python, Sublime]
---

Recently, a feature I use relatively often in my day to day use of Sublime Text, the "Open in a New Window" command stopped working. It turns out this is not a default feature of Sublime Text, but supplied by the plugin [SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements). The issue appears to come from a change in default behavior of the `subl` command which now will attempt to open a directory within an open project window if one contains that directory. A fix was easy enough, which I [PR'd here](https://github.com/titoBouzout/SideBarEnhancements/pull/432), but sadly appears to be unmaintained for the past couple years, so I'm not sure when the maintainer will get around to merging it.

If you want to incorporate this fix into your own installation, you can edit the [two lines the same as I have](https://github.com/titoBouzout/SideBarEnhancements/pull/432/files#diff-3bf65b4d258adc64df0c828114bb3a13959df4cb5caf897171bd880b06675ba7). If you have the [PackageResourceViewer](https://github.com/skuroda/PackageResourceViewer) plugin installed, it is easy enough to edit the package in place.
