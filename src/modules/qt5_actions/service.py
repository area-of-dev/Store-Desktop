# -*- coding: utf-8 -*-
# Copyright 2015 Alex Woroschilow (alex.woroschilow@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import hexdi

from .storage.interface import ActionsStorage
from .workspace.dashboard import DashboardWidget
from .workspace.thread import WorkspaceThread


@hexdi.permanent('workspace.actions')
class DashboardWidgetInstance(DashboardWidget):
    pass


@hexdi.permanent('thread.actions')
class WorkspaceThreadInstance(WorkspaceThread):
    pass


@hexdi.permanent('actions')
class ActionsStorageInstance(ActionsStorage):

    def install(self, model):
        entity = self.add_action({
            'action': 'install',
            'package': model,
        })

        print(self, entity)

    def download(self, model):
        entity = self.add_action({
            'action': 'download',
            'package': model,
        })

        print(self, entity)

    def validate(self, model):
        entity = self.add_action({
            'action': 'validate',
            'package': model,
        })

        print(self, entity)

    def integrate(self, model):
        entity = self.add_action({
            'action': 'integrate',
            'appimage': model,
        })

        print(self, entity)

    def remove(self, model):
        entity = self.add_action({
            'action': 'remove',
            'appimage': model,
        })
        print(self, entity)

    def start(self, model):
        entity = self.add_action({
            'action': 'start',
            'appimage': model,
        })
        print(self, entity)
