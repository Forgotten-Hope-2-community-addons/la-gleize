# Common plugins
from game.plugins import plugin, limitKit, teamSPs, ticketLoss, NCOrifleData
# Gameplay plugins
from game.plugins import push, linkCPs

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

# -------------------------------------------------- #
#   64p layer configuration
# -------------------------------------------------- #

# 64p layer flags
flags_64 = {
    'mains': {
        'axis': 'cp_64_la_gleize_axis_main',
        'allies': 'cp_64_la_gleize_allied_main',
    },
    's1': {
        'name': 'defense_line',
        'flags': [
            'cp_64_la_gleize_chapel',
            'cp_64_la_gleize_crash_site',
            'cp_64_la_gleize_station'
        ],
        'lock': 'cp_64_la_gleize_s1_lock',
    },
    's2': {
        'name': 'la_gleize',
        'flags': [
            'cp_64_la_gleize_defense_line',
            'cp_64_la_gleize_crossroads',
            'cp_64_la_gleize_church'
        ],
        'lock': 'cp_64_la_gleize_s2_lock',
    },
    's3': {
        'name': 'last_stand',
        'flags': [
            'cp_64_la_gleize_river_farm',
            'cp_64_la_gleize_werimont'
        ],
        'lock': 'cp_64_la_gleize_axis_main',
    },
}

# Sector locks. Dummy flags.
lock_64 = [
    plugin(
        linkCPs,
        target = flags_64['s1']['lock'],
        source = flags_64['s1']['flags'],
    ),
    plugin(
        linkCPs,
        target = flags_64['s2']['lock'],
        source = flags_64['s2']['flags'],
    ),
    plugin(
        linkCPs,
        target = flags_64['s3']['lock'],
        source = flags_64['s3']['flags'],
    ),
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

# Unlock La Gleize sector once the forest line is lost
push_64 = [
    # Sector 1: defense line
    plugin(
        push,
        source = flags_64['s1']['flags'],
        target = flags_64['s1']['lock'],
        attacker = 2,
        display_arrow = True
    ),
    # Sector 2: La Gleize
    plugin(
        push,
        source = flags_64['s1']['lock'],
        target = flags_64['s2']['flags'],
        attacker = 2,
        display_arrow = True,
        delay = 15
    ),
    plugin(
        push,
        source = flags_64['s2']['flags'],
        target = flags_64['s2']['lock'],
        attacker = 2,
        display_arrow = True
    ),
    # Sector 3: last stand
    plugin(
        push,
        source = flags_64['s2']['lock'],
        target = flags_64['s3']['flags'],
        attacker = 2,
        display_arrow = True,
        delay = 15
    ),
]

gpm_cq = {
  64: rifleNCO + spawns + kit_limits_64 + ticket_loss_64 + push_64,
}

# -------------------------------------------------- #
#   32p plugins
# -------------------------------------------------- #

# Kit limits for the 32p layer
# kit_limits_32 = [
#   plugin(
#     limitKit,
#     team = 1,
#     slot = 1,
#     kit = 'GW_SMGAssault_Limited',
#     limit = 0.2
#   ),
#   plugin(
#     limitKit,
#     team = 2,
#     slot = 1,
#     kit = 'UW_SMGAssault_Limited_para',
#     limit = 0.2
#   ),
#   plugin(
#     limitKit,
#     team = 1,
#     slot = 3,
#     kit = 'GW_LMG_Limited',
#     limit = 0.1
#   ),
# ]

# # Ticket loss per minute
# ticket_loss_32 = [
#   plugin(ticketLoss, ticketLoss1 = 7, ticketLoss2 = 4)
# ]

# # Push 32. Axis counter-attack attempt on D-Day at 09:30h
# push_32 = [
#   plugin(
#     push,
#     source = 'CP_32_SME_RoadToCarentan',
#     target = 'CP_32_SME_RoadToLaFiere',
#     attacker = 1,
#     display_arrow = False
#   ),
#   # plugin(
#   #   push,
#   #   source = 'CP_32_SME_Church',
#   #   target = 'CP_32_SME_RoadToLaFiere',
#   #   attacker = 1,
#   #   display_arrow = False
#   # ),
#   # plugin(
#   #   push,
#   #   source = 'CP_32_SME_RoadToCarentan',
#   #   target = 'CP_32_SME_RoadToUtahBeach',
#   #   attacker = 1,
#   #   display_arrow = False
#   # ),
#   plugin(
#     push,
#     source = 'CP_32_SME_Church',
#     target = 'CP_32_SME_RoadToUtahBeach',
#     attacker = 1,
#     display_arrow = False
#   ),

#   plugin(
#     push,
#     source = 'CP_32_SME_RoadToLaFiere',
#     target = 'CP_32_SME_TownHall',
#     attacker = 1,
#     display_arrow = False
#   ),
#   # plugin(
#   #   push,
#   #   source = 'CP_32_SME_RoadToUtahBeach',
#   #   target = 'CP_32_SME_TownHall',
#   #   attacker = 1,
#   #   display_arrow = False
#   # ),
#   plugin(
#     push,
#     source = 'CP_32_SME_RoadToLaFiere',
#     target = 'CP_32_SME_Hospital',
#     attacker = 1,
#     display_arrow = False
#   ),
#   plugin(
#     push,
#     source = 'CP_32_SME_RoadToUtahBeach',
#     target = 'CP_32_SME_Hospital',
#     attacker = 1,
#     display_arrow = False
#   ),
# ]

# # -------------------------------------------------- #
# #   16p plugins
# # -------------------------------------------------- #

# # Kit limits for the 16p layer
# kit_limits_16 = [
#   plugin(
#     limitKit,
#     team = 1,
#     slot = 1,
#     kit = 'GW_SMGAssault_Limited',
#     limit = 0.3
#   ),
#   plugin(
#     limitKit,
#     team = 2,
#     slot = 1,
#     kit = 'UW_SMGAssault_Limited_para',
#     limit = 0.3
#   ),
#   plugin(
#     limitKit,
#     team = 1,
#     slot = 3,
#     kit = 'GW_LMG_Limited',
#     limit = 0.1
#   ),
# ]

# # Ticket loss per minute.
# ticket_loss_16 = [
#   plugin(ticketLoss, ticketLoss1 = 12, ticketLoss2 = 10)
# ]

# # Push 16. Axis counter-attack attempt on D-Day+1 at 13:00h
# push_16 = [
#   plugin(
#     push,
#     source = "CP_16_SME_AxisMain",
#     target = "CP_16_SME_Hospital",
#     attacker = 1,
#     display_arrow = True
#   ),
#   plugin(
#     push,
#     source = "CP_16_SME_Hospital",
#     target = "CP_16_SME_TownHall",
#     attacker = 1,
#     display_arrow = True
#   ),
#   plugin(
#     push,
#     source = "CP_16_SME_TownHall",
#     target = "CP_16_SME_Church",
#     attacker = 1,
#     display_arrow = True
#   ),
# ]

# -------------------------------------------------- #
#   Gameplay configuration
# -------------------------------------------------- #
# gpm_cq = {
#   64: rifleNCO + spawns + kit_limits_64 + ticket_loss_64 + push_64,
#   32: rifleNCO + spawns + kit_limits_32 + ticket_loss_32 + push_32,
#   16: rifleNCO + spawns + kit_limits_16 + ticket_loss_16 + push_16,
# }
