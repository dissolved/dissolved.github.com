---
layout: post
title: Fixing Sublime Text's SideBarEnhancements Plugin
categories: [Python, Sublime]
last_modified_at: 2026-10-13
excerpt: "How I fixed SideBarEnhancements' Open in a New Window command, with an update on the upstream fix that was merged in 2021."
description: A historical Sublime Text sidebar workaround, with an update on the merged upstream fix.
---

> **Update — October 13, 2026:** [PR #432](https://github.com/titoBouzout/SideBarEnhancements/pull/432) was merged on August 23, 2021. This post documents the original issue and fix; update SideBarEnhancements before considering a manual package edit. I have not retested the workaround against current Sublime Text releases.

Recently, a feature I use relatively often in my day to day use of Sublime Text, the "Open in a New Window" command stopped working. It turns out this is not a default feature of Sublime Text, but supplied by the plugin [SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements). The issue appears to come from a change in default behavior of the `subl` command which now will attempt to open a directory within an open project window if one contains that directory. A fix was easy enough, which I [PR'd here](https://github.com/titoBouzout/SideBarEnhancements/pull/432), which was awaiting review when I wrote this post.

If you want to incorporate this fix into your own installation, you can edit the [two lines the same as I have](https://github.com/titoBouzout/SideBarEnhancements/pull/432/files#diff-3bf65b4d258adc64df0c828114bb3a13959df4cb5caf897171bd880b06675ba7). If you have the [PackageResourceViewer](https://github.com/skuroda/PackageResourceViewer) plugin installed, it is easy enough to edit the package in place.
