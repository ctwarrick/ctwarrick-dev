// infra/dns.bicep — the Azure DNS zone for ctwarrick.dev, deployed into the
// resource group created by main.bicep.
//
// Why: GoDaddy can't flatten apex records, so DNS is delegated to this Azure
// DNS zone (research.md §7). Delegation is done once at the registrar by
// pointing GoDaddy's nameservers at this zone's `nameServers` output. The apex
// and `www` custom-domain bindings are then added on the Static Web App via the
// portal's "Custom Domain on Azure DNS" flow — they are intentionally NOT
// modeled here because the apex `dns-txt-token` validation token is not exposed
// as a Bicep/ARM output, so a single-pass declarative bind deadlocks in
// "Validating" (Azure/static-web-apps#1652). This module owns the zone; the
// bindings (and the TXT/ALIAS/CNAME records the portal auto-creates inside it)
// are applied imperatively.

@description('DNS zone (apex domain) name, e.g. ctwarrick.dev.')
param dnsZoneName string

resource dnsZone 'Microsoft.Network/dnsZones@2018-05-01' = {
  name: dnsZoneName
  location: 'global'
}

@description('The Azure nameservers for the zone — set these at the registrar (GoDaddy) to delegate DNS.')
output nameServers array = dnsZone.properties.nameServers
