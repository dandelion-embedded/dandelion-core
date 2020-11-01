# Dandelion Core
## Introduction
Dandelion Core is almost an operating system. It defines a standard structure for downloading, storing and executing Micropython apps on an M5Stack Core 2.
It is based on [lvgl](https://github.com/lvgl/lvgl) and needs an underlying Micropython firmware such as [this one](https://github.com/imliubo/M5Stack-Micropython).

It is not focused on speed, but it aims to be a simple, complete and well-organized way to develop GUI apps. In other words, it should be usable as the base of an universal tool, with the same flexibility as a modern smartphone, but done in Micropython and under your complete control.

The Core the midway point between the stem and the Dandelion's many seeds. The seeds are individually different, but every one of them is still collectively recognizable as a seed. In the same analogy, the final user should have a variety of different apps, but every one of them should follow the standard behaviours and styles defined by the Core. There are a few applications that shouldn't be detached from the Core, such as a launcher, a settings app and, in the future, a portal for updating and downloading other software. These apps, as I said, shouldn't be removed, but nothing should stop you from creating your own.

If you are interested in this project, your help is welcome. No experience is required, matter-of-fact, I'm a beginner in Micropython.

## Progress
- [x] Basic Micropython firmware with LCD and touchscreen support
- [x] Application discovery
- [x] Launcher detection and bootstrapping
- [ ] Springboard application
- [ ] Standardized application manifest and structure
- [ ] Boot screen
- [ ] Settings application
- [ ] Boilerplate application
- [ ] Development tools (manifest generation, automatic checks, caller inspection, versioning, ...)
- [ ] Documentation
- [ ] Web infrastructure for Store
- [ ] Store application
- [ ] OOBE
- [ ] Smartphone application for Core
- [ ] Standard launch system between Dandelion applications
- [ ] Standard communication system between smartphone and Dandelion applications
- [ ] Additional Micropython drivers
- [ ] Porting to other ESP32-based boards
- [ ] Remote editor