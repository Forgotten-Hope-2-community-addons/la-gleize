# Common plugins
from game.plugins import plugin, limitKit, teamSPs, ticketLoss, NCOrifleData

# -------------------------------------------------- #
#   Common plugins
# -------------------------------------------------- #

# Officer kit
rifleNCO = [
  plugin(NCOrifleData, kits = ('GS_NCO_mp40_g43', 'UW_NCO'))
]

# Team Spawns
spawns = [
  plugin(teamSPs), # Auto-fill
]

# Kit limits for the 64p layer
kit_limits_64 = [
  plugin(
    limitKit,
    team = 1,
    slot = 1,
    kit = 'GW_StG44Assault_Limited',
    limit = 0.2
  ),
  plugin(
    limitKit,
    team = 2,
    slot = 1,
    kit = 'UW_SMGAssault_Limited',
    limit = 0.2
  ),
  plugin(
    limitKit,
    team = 1,
    slot = 3,
    kit = 'GW_LMG_MG42_Limited',
    limit = 0.1
  ),
  plugin(
    limitKit,
    team = 2,
    slot = 3,
    kit = 'UW_LMG_Limited',
    limit = 0.1
  ),
  plugin(
    limitKit,
    team = 1,
    slot = 5,
    kit = 'GW_AntitankAssault60m_Limited',
    limit = 0.1
  ),
  plugin(
    limitKit,
    team = 2,
    slot = 5,
    kit = 'UW_AntitankAssault_Limited',
    limit = 0.1
  ),
]

# Ticket loss per minute
ticket_loss_64 = [
  plugin(ticketLoss, ticketLoss1 = 20, ticketLoss2 = 20)
]

gpm_cq = {
  64: rifleNCO + spawns + kit_limits_64 + ticket_loss_64,
  32: rifleNCO + spawns + kit_limits_64 + ticket_loss_64,
}
