# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Schedule(Model):
    """The schedule according to which jobs will be created.

    :param do_not_run_until: The earliest time at which any job may be
     created under this job schedule. If you do not specify a doNotRunUntil
     time, the schedule becomes ready to create jobs immediately.
    :type do_not_run_until: datetime
    :param do_not_run_after: A time after which no job will be created under
     this job schedule. The schedule will move to the completed state as soon
     as this deadline is past and there is no active job under this job
     schedule.
    :type do_not_run_after: datetime
    :param start_window: The time interval, starting from the time at which
     the schedule indicates a job should be created, within which a job must
     be created. If a job is not created within the startWindow interval,
     then the 'opportunity' is lost; no job will be created until the next
     recurrence of the schedule.
    :type start_window: timedelta
    :param recurrence_interval: The time interval between the start times of
     two successive jobs under the job schedule. A job schedule can have at
     most one active job under it at any given time.
    :type recurrence_interval: timedelta
    """ 

    _attribute_map = {
        'do_not_run_until': {'key': 'doNotRunUntil', 'type': 'iso-8601'},
        'do_not_run_after': {'key': 'doNotRunAfter', 'type': 'iso-8601'},
        'start_window': {'key': 'startWindow', 'type': 'duration'},
        'recurrence_interval': {'key': 'recurrenceInterval', 'type': 'duration'},
    }

    def __init__(self, do_not_run_until=None, do_not_run_after=None, start_window=None, recurrence_interval=None):
        self.do_not_run_until = do_not_run_until
        self.do_not_run_after = do_not_run_after
        self.start_window = start_window
        self.recurrence_interval = recurrence_interval
