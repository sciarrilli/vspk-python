# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from bambou import NURESTObject


class NUNetworkPerformanceBinding(NURESTObject):
    """ Represents a NetworkPerformanceBinding in the VSD

        Notes:
            None
    """

    __rest_name__ = "networkperformancebinding"
    __resource_name__ = "networkperformancebindings"

    

    def __init__(self, **kwargs):
        """ Initializes a NetworkPerformanceBinding instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> networkperformancebinding = NUNetworkPerformanceBinding(id=u'xxxx-xxx-xxx-xxx', name=u'NetworkPerformanceBinding')
                >>> networkperformancebinding = NUNetworkPerformanceBinding(data=my_dict)
        """

        super(NUNetworkPerformanceBinding, self).__init__()

        # Read/Write Attributes
        
        self._read_only = None
        self._priority = None
        self._associated_network_measurement_id = None
        
        self.expose_attribute(local_name="read_only", remote_name="readOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=True)
        self.expose_attribute(local_name="associated_network_measurement_id", remote_name="associatedNetworkMeasurementID", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def read_only(self):
        """ Get read_only value.

            Notes:
                Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """ Set read_only value.

            Notes:
                Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        self._read_only = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                Priority of the associated Network Performance Measurement

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                Priority of the associated Network Performance Measurement

                
        """
        self._priority = value

    
    @property
    def associated_network_measurement_id(self):
        """ Get associated_network_measurement_id value.

            Notes:
                Associated Network Performance Measurement UD

                
                This attribute is named `associatedNetworkMeasurementID` in VSD API.
                
        """
        return self._associated_network_measurement_id

    @associated_network_measurement_id.setter
    def associated_network_measurement_id(self, value):
        """ Set associated_network_measurement_id value.

            Notes:
                Associated Network Performance Measurement UD

                
                This attribute is named `associatedNetworkMeasurementID` in VSD API.
                
        """
        self._associated_network_measurement_id = value

    

    