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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUDomainFIPAclTemplateEntry(NURESTObject):
    """ Represents a DomainFIPAclTemplateEntry in the VSD

        Notes:
            Defines the template of Egress Domain ACL Template entries
    """

    __rest_name__ = "egressdomainfloatingipaclentrytemplate"
    __resource_name__ = "egressdomainfloatingipaclentrytemplates"

    
    ## Constants
    
    CONST_NETWORK_TYPE_NETWORK_MACRO_GROUP = "NETWORK_MACRO_GROUP"
    
    CONST_ACTION_DROP = "DROP"
    
    CONST_LOCATION_TYPE_ZONE = "ZONE"
    
    CONST_ACTION_REDIRECT = "REDIRECT"
    
    CONST_DESTINATION_TYPE_NETWORK = "NETWORK"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_NETWORK_TYPE_PUBLIC_NETWORK = "PUBLIC_NETWORK"
    
    CONST_ACTION_FORWARD = "FORWARD"
    
    CONST_NETWORK_TYPE_POLICYGROUP = "POLICYGROUP"
    
    CONST_LOCATION_TYPE_ANY = "ANY"
    
    CONST_SOURCE_TYPE_POLICYGROUP = "POLICYGROUP"
    
    CONST_NETWORK_TYPE_ENDPOINT_DOMAIN = "ENDPOINT_DOMAIN"
    
    CONST_SOURCE_TYPE_NETWORKPOLICYGROUP = "NETWORKPOLICYGROUP"
    
    CONST_NETWORK_TYPE_ENTERPRISE_NETWORK = "ENTERPRISE_NETWORK"
    
    CONST_NETWORK_TYPE_ANY = "ANY"
    
    CONST_LOCATION_TYPE_POLICYGROUP = "POLICYGROUP"
    
    CONST_NETWORK_TYPE_SUBNET = "SUBNET"
    
    CONST_NETWORK_TYPE_ZONE = "ZONE"
    
    CONST_DESTINATION_TYPE_NETWORKPOLICYGROUP = "NETWORKPOLICYGROUP"
    
    CONST_NETWORK_TYPE_ENDPOINT_SUBNET = "ENDPOINT_SUBNET"
    
    CONST_SOURCE_TYPE_NETWORK = "NETWORK"
    
    CONST_LOCATION_TYPE_VPORTTAG = "VPORTTAG"
    
    CONST_LOCATION_TYPE_SUBNET = "SUBNET"
    
    CONST_POLICY_STATE_DRAFT = "DRAFT"
    
    CONST_LOCATION_TYPE_REDIRECTIONTARGET = "REDIRECTIONTARGET"
    
    CONST_POLICY_STATE_LIVE = "LIVE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_NETWORK_TYPE_INTERNET_POLICYGROUP = "INTERNET_POLICYGROUP"
    
    CONST_NETWORK_TYPE_ENDPOINT_ZONE = "ENDPOINT_ZONE"
    
    CONST_DESTINATION_TYPE_POLICYGROUP = "POLICYGROUP"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DomainFIPAclTemplateEntry instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> domainfipacltemplateentry = NUDomainFIPAclTemplateEntry(id=u'xxxx-xxx-xxx-xxx', name=u'DomainFIPAclTemplateEntry')
                >>> domainfipacltemplateentry = NUDomainFIPAclTemplateEntry(data=my_dict)
        """

        super(NUDomainFIPAclTemplateEntry, self).__init__()

        # Read/Write Attributes
        
        self._acl_template_name = None
        self._icmp_code = None
        self._icmp_type = None
        self._ipv6_address_override = None
        self._dscp = None
        self._last_updated_by = None
        self._action = None
        self._action_details = None
        self._address_override = None
        self._description = None
        self._dest_pg_id = None
        self._dest_pg_type = None
        self._destination_port = None
        self._destination_type = None
        self._destination_value = None
        self._network_id = None
        self._network_type = None
        self._mirror_destination_id = None
        self._flow_logging_enabled = None
        self._enterprise_name = None
        self._entity_scope = None
        self._location_id = None
        self._location_type = None
        self._policy_state = None
        self._domain_name = None
        self._source_pg_id = None
        self._source_pg_type = None
        self._source_port = None
        self._source_type = None
        self._source_value = None
        self._priority = None
        self._protocol = None
        self._associated_live_entity_id = None
        self._stateful = None
        self._stats_id = None
        self._stats_logging_enabled = None
        self._ether_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="acl_template_name", remote_name="ACLTemplateName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="icmp_code", remote_name="ICMPCode", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="icmp_type", remote_name="ICMPType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipv6_address_override", remote_name="IPv6AddressOverride", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dscp", remote_name="DSCP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="action", remote_name="action", attribute_type=str, is_required=False, is_unique=False, choices=[u'DROP', u'FORWARD', u'REDIRECT'])
        self.expose_attribute(local_name="action_details", remote_name="actionDetails", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address_override", remote_name="addressOverride", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dest_pg_id", remote_name="destPgId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dest_pg_type", remote_name="destPgType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_port", remote_name="destinationPort", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_type", remote_name="destinationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'NETWORK', u'NETWORKPOLICYGROUP', u'POLICYGROUP'])
        self.expose_attribute(local_name="destination_value", remote_name="destinationValue", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_id", remote_name="networkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_type", remote_name="networkType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ANY', u'ENDPOINT_DOMAIN', u'ENDPOINT_SUBNET', u'ENDPOINT_ZONE', u'ENTERPRISE_NETWORK', u'INTERNET_POLICYGROUP', u'NETWORK_MACRO_GROUP', u'POLICYGROUP', u'PUBLIC_NETWORK', u'SUBNET', u'ZONE'])
        self.expose_attribute(local_name="mirror_destination_id", remote_name="mirrorDestinationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_logging_enabled", remote_name="flowLoggingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_name", remote_name="enterpriseName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="location_id", remote_name="locationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="location_type", remote_name="locationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ANY', u'POLICYGROUP', u'REDIRECTIONTARGET', u'SUBNET', u'VPORTTAG', u'ZONE'])
        self.expose_attribute(local_name="policy_state", remote_name="policyState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DRAFT', u'LIVE'])
        self.expose_attribute(local_name="domain_name", remote_name="domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="source_pg_id", remote_name="sourcePgId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="source_pg_type", remote_name="sourcePgType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="source_port", remote_name="sourcePort", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="source_type", remote_name="sourceType", attribute_type=str, is_required=False, is_unique=False, choices=[u'NETWORK', u'NETWORKPOLICYGROUP', u'POLICYGROUP'])
        self.expose_attribute(local_name="source_value", remote_name="sourceValue", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="protocol", remote_name="protocol", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_live_entity_id", remote_name="associatedLiveEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stateful", remote_name="stateful", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_id", remote_name="statsID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_logging_enabled", remote_name="statsLoggingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ether_type", remote_name="etherType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def acl_template_name(self):
        """ Get acl_template_name value.

            Notes:
                The name of the parent Template for this acl entry

                
                This attribute is named `ACLTemplateName` in VSD API.
                
        """
        return self._acl_template_name

    @acl_template_name.setter
    def acl_template_name(self, value):
        """ Set acl_template_name value.

            Notes:
                The name of the parent Template for this acl entry

                
                This attribute is named `ACLTemplateName` in VSD API.
                
        """
        self._acl_template_name = value

    
    @property
    def icmp_code(self):
        """ Get icmp_code value.

            Notes:
                The ICMP Code when protocol selected is ICMP

                
                This attribute is named `ICMPCode` in VSD API.
                
        """
        return self._icmp_code

    @icmp_code.setter
    def icmp_code(self, value):
        """ Set icmp_code value.

            Notes:
                The ICMP Code when protocol selected is ICMP

                
                This attribute is named `ICMPCode` in VSD API.
                
        """
        self._icmp_code = value

    
    @property
    def icmp_type(self):
        """ Get icmp_type value.

            Notes:
                The ICMP Type when protocol selected is ICMP

                
                This attribute is named `ICMPType` in VSD API.
                
        """
        return self._icmp_type

    @icmp_type.setter
    def icmp_type(self, value):
        """ Set icmp_type value.

            Notes:
                The ICMP Type when protocol selected is ICMP

                
                This attribute is named `ICMPType` in VSD API.
                
        """
        self._icmp_type = value

    
    @property
    def ipv6_address_override(self):
        """ Get ipv6_address_override value.

            Notes:
                Overrides the source IPv6 for Ingress and destination IP for Egress, MAC entries will use this address as the match criteria.

                
                This attribute is named `IPv6AddressOverride` in VSD API.
                
        """
        return self._ipv6_address_override

    @ipv6_address_override.setter
    def ipv6_address_override(self, value):
        """ Set ipv6_address_override value.

            Notes:
                Overrides the source IPv6 for Ingress and destination IP for Egress, MAC entries will use this address as the match criteria.

                
                This attribute is named `IPv6AddressOverride` in VSD API.
                
        """
        self._ipv6_address_override = value

    
    @property
    def dscp(self):
        """ Get dscp value.

            Notes:
                DSCP match condition to be set in the rule. It is either * or from 0-63

                
                This attribute is named `DSCP` in VSD API.
                
        """
        return self._dscp

    @dscp.setter
    def dscp(self, value):
        """ Set dscp value.

            Notes:
                DSCP match condition to be set in the rule. It is either * or from 0-63

                
                This attribute is named `DSCP` in VSD API.
                
        """
        self._dscp = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def action(self):
        """ Get action value.

            Notes:
                The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry

                
        """
        return self._action

    @action.setter
    def action(self, value):
        """ Set action value.

            Notes:
                The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry

                
        """
        self._action = value

    
    @property
    def action_details(self):
        """ Get action_details value.

            Notes:
                Type of action to be performed when a ACL match criteria succeeds

                
                This attribute is named `actionDetails` in VSD API.
                
        """
        return self._action_details

    @action_details.setter
    def action_details(self, value):
        """ Set action_details value.

            Notes:
                Type of action to be performed when a ACL match criteria succeeds

                
                This attribute is named `actionDetails` in VSD API.
                
        """
        self._action_details = value

    
    @property
    def address_override(self):
        """ Get address_override value.

            Notes:
                Overrides the source IP for Ingress and destination IP for Egress, MAC entries will use this address as the match criteria.

                
                This attribute is named `addressOverride` in VSD API.
                
        """
        return self._address_override

    @address_override.setter
    def address_override(self, value):
        """ Set address_override value.

            Notes:
                Overrides the source IP for Ingress and destination IP for Egress, MAC entries will use this address as the match criteria.

                
                This attribute is named `addressOverride` in VSD API.
                
        """
        self._address_override = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the ACL entry

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the ACL entry

                
        """
        self._description = value

    
    @property
    def dest_pg_id(self):
        """ Get dest_pg_id value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `destPgId` in VSD API.
                
        """
        return self._dest_pg_id

    @dest_pg_id.setter
    def dest_pg_id(self, value):
        """ Set dest_pg_id value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `destPgId` in VSD API.
                
        """
        self._dest_pg_id = value

    
    @property
    def dest_pg_type(self):
        """ Get dest_pg_type value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `destPgType` in VSD API.
                
        """
        return self._dest_pg_type

    @dest_pg_type.setter
    def dest_pg_type(self, value):
        """ Set dest_pg_type value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `destPgType` in VSD API.
                
        """
        self._dest_pg_type = value

    
    @property
    def destination_port(self):
        """ Get destination_port value.

            Notes:
                The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range

                
                This attribute is named `destinationPort` in VSD API.
                
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, value):
        """ Set destination_port value.

            Notes:
                The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range

                
                This attribute is named `destinationPort` in VSD API.
                
        """
        self._destination_port = value

    
    @property
    def destination_type(self):
        """ Get destination_type value.

            Notes:
                Network Type - either PolicyGroup or Network

                
                This attribute is named `destinationType` in VSD API.
                
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, value):
        """ Set destination_type value.

            Notes:
                Network Type - either PolicyGroup or Network

                
                This attribute is named `destinationType` in VSD API.
                
        """
        self._destination_type = value

    
    @property
    def destination_value(self):
        """ Get destination_value value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `destinationValue` in VSD API.
                
        """
        return self._destination_value

    @destination_value.setter
    def destination_value(self, value):
        """ Set destination_value value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `destinationValue` in VSD API.
                
        """
        self._destination_value = value

    
    @property
    def network_id(self):
        """ Get network_id value.

            Notes:
                The destination network entity that is referenced(subnet/zone/macro)

                
                This attribute is named `networkID` in VSD API.
                
        """
        return self._network_id

    @network_id.setter
    def network_id(self, value):
        """ Set network_id value.

            Notes:
                The destination network entity that is referenced(subnet/zone/macro)

                
                This attribute is named `networkID` in VSD API.
                
        """
        self._network_id = value

    
    @property
    def network_type(self):
        """ Get network_type value.

            Notes:
                Type of the source network -    VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY

                
                This attribute is named `networkType` in VSD API.
                
        """
        return self._network_type

    @network_type.setter
    def network_type(self, value):
        """ Set network_type value.

            Notes:
                Type of the source network -    VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY

                
                This attribute is named `networkType` in VSD API.
                
        """
        self._network_type = value

    
    @property
    def mirror_destination_id(self):
        """ Get mirror_destination_id value.

            Notes:
                This is the ID of the mirrorDestination entity associated with this entity

                
                This attribute is named `mirrorDestinationID` in VSD API.
                
        """
        return self._mirror_destination_id

    @mirror_destination_id.setter
    def mirror_destination_id(self, value):
        """ Set mirror_destination_id value.

            Notes:
                This is the ID of the mirrorDestination entity associated with this entity

                
                This attribute is named `mirrorDestinationID` in VSD API.
                
        """
        self._mirror_destination_id = value

    
    @property
    def flow_logging_enabled(self):
        """ Get flow_logging_enabled value.

            Notes:
                Is flow logging enabled for this particular template

                
                This attribute is named `flowLoggingEnabled` in VSD API.
                
        """
        return self._flow_logging_enabled

    @flow_logging_enabled.setter
    def flow_logging_enabled(self, value):
        """ Set flow_logging_enabled value.

            Notes:
                Is flow logging enabled for this particular template

                
                This attribute is named `flowLoggingEnabled` in VSD API.
                
        """
        self._flow_logging_enabled = value

    
    @property
    def enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                The name of the enterprise for the domains parent

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                The name of the enterprise for the domains parent

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def location_id(self):
        """ Get location_id value.

            Notes:
                The ID of the location entity (Subnet/Zone/VportTag)

                
                This attribute is named `locationID` in VSD API.
                
        """
        return self._location_id

    @location_id.setter
    def location_id(self, value):
        """ Set location_id value.

            Notes:
                The ID of the location entity (Subnet/Zone/VportTag)

                
                This attribute is named `locationID` in VSD API.
                
        """
        self._location_id = value

    
    @property
    def location_type(self):
        """ Get location_type value.

            Notes:
                Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG

                
                This attribute is named `locationType` in VSD API.
                
        """
        return self._location_type

    @location_type.setter
    def location_type(self, value):
        """ Set location_type value.

            Notes:
                Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG

                
                This attribute is named `locationType` in VSD API.
                
        """
        self._location_type = value

    
    @property
    def policy_state(self):
        """ Get policy_state value.

            Notes:
                State of the policy. 

                
                This attribute is named `policyState` in VSD API.
                
        """
        return self._policy_state

    @policy_state.setter
    def policy_state(self, value):
        """ Set policy_state value.

            Notes:
                State of the policy. 

                
                This attribute is named `policyState` in VSD API.
                
        """
        self._policy_state = value

    
    @property
    def domain_name(self):
        """ Get domain_name value.

            Notes:
                The name of the domain/domain template for the aclTemplateNames parent

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """ Set domain_name value.

            Notes:
                The name of the domain/domain template for the aclTemplateNames parent

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    
    @property
    def source_pg_id(self):
        """ Get source_pg_id value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `sourcePgId` in VSD API.
                
        """
        return self._source_pg_id

    @source_pg_id.setter
    def source_pg_id(self, value):
        """ Set source_pg_id value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `sourcePgId` in VSD API.
                
        """
        self._source_pg_id = value

    
    @property
    def source_pg_type(self):
        """ Get source_pg_type value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `sourcePgType` in VSD API.
                
        """
        return self._source_pg_type

    @source_pg_type.setter
    def source_pg_type(self, value):
        """ Set source_pg_type value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `sourcePgType` in VSD API.
                
        """
        self._source_pg_type = value

    
    @property
    def source_port(self):
        """ Get source_port value.

            Notes:
                Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range

                
                This attribute is named `sourcePort` in VSD API.
                
        """
        return self._source_port

    @source_port.setter
    def source_port(self, value):
        """ Set source_port value.

            Notes:
                Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range

                
                This attribute is named `sourcePort` in VSD API.
                
        """
        self._source_port = value

    
    @property
    def source_type(self):
        """ Get source_type value.

            Notes:
                Location Type - either PolicyGroup or Network

                
                This attribute is named `sourceType` in VSD API.
                
        """
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        """ Set source_type value.

            Notes:
                Location Type - either PolicyGroup or Network

                
                This attribute is named `sourceType` in VSD API.
                
        """
        self._source_type = value

    
    @property
    def source_value(self):
        """ Get source_value value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `sourceValue` in VSD API.
                
        """
        return self._source_value

    @source_value.setter
    def source_value(self, value):
        """ Set source_value value.

            Notes:
                In case of PG this will be its EVPNBGPCommunity String, incase of network it will be network cidr

                
                This attribute is named `sourceValue` in VSD API.
                
        """
        self._source_value = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                The priority of the ACL entry that determines the order of entries

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                The priority of the ACL entry that determines the order of entries

                
        """
        self._priority = value

    
    @property
    def protocol(self):
        """ Get protocol value.

            Notes:
                Protocol number that must be matched

                
        """
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        """ Set protocol value.

            Notes:
                Protocol number that must be matched

                
        """
        self._protocol = value

    
    @property
    def associated_live_entity_id(self):
        """ Get associated_live_entity_id value.

            Notes:
                ID of the associated live entity

                
                This attribute is named `associatedLiveEntityID` in VSD API.
                
        """
        return self._associated_live_entity_id

    @associated_live_entity_id.setter
    def associated_live_entity_id(self, value):
        """ Set associated_live_entity_id value.

            Notes:
                ID of the associated live entity

                
                This attribute is named `associatedLiveEntityID` in VSD API.
                
        """
        self._associated_live_entity_id = value

    
    @property
    def stateful(self):
        """ Get stateful value.

            Notes:
                True means that this ACL entry is stateful, so there will be a corresponding rule that will be created by OVS in the network. False means that there is no corresponding rule created by OVS in the network.

                
        """
        return self._stateful

    @stateful.setter
    def stateful(self, value):
        """ Set stateful value.

            Notes:
                True means that this ACL entry is stateful, so there will be a corresponding rule that will be created by OVS in the network. False means that there is no corresponding rule created by OVS in the network.

                
        """
        self._stateful = value

    
    @property
    def stats_id(self):
        """ Get stats_id value.

            Notes:
                The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD

                
                This attribute is named `statsID` in VSD API.
                
        """
        return self._stats_id

    @stats_id.setter
    def stats_id(self, value):
        """ Set stats_id value.

            Notes:
                The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD

                
                This attribute is named `statsID` in VSD API.
                
        """
        self._stats_id = value

    
    @property
    def stats_logging_enabled(self):
        """ Get stats_logging_enabled value.

            Notes:
                Is stats logging enabled for this particular template

                
                This attribute is named `statsLoggingEnabled` in VSD API.
                
        """
        return self._stats_logging_enabled

    @stats_logging_enabled.setter
    def stats_logging_enabled(self, value):
        """ Set stats_logging_enabled value.

            Notes:
                Is stats logging enabled for this particular template

                
                This attribute is named `statsLoggingEnabled` in VSD API.
                
        """
        self._stats_logging_enabled = value

    
    @property
    def ether_type(self):
        """ Get ether_type value.

            Notes:
                Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

                
                This attribute is named `etherType` in VSD API.
                
        """
        return self._ether_type

    @ether_type.setter
    def ether_type(self, value):
        """ Set ether_type value.

            Notes:
                Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

                
                This attribute is named `etherType` in VSD API.
                
        """
        self._ether_type = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    