# coding: utf-8

from gendefs_js import *

CLIENT_PACKETS = []
CLIENT_GM_PACKETS = []
SERVER_PACKETS = []

NUMSKILLS = 20



CLIENT_PACKETS.append(Packet('LoginExistingChar', [
    ('UserName', TYPE_UNICODE_STRING), 
    ('Password', TYPE_UNICODE_STRING),
    ('VerA', TYPE_I8),
    ('VerB', TYPE_I8),
    ('VerC', TYPE_I8),
    ],))
CLIENT_PACKETS.append(Packet('ThrowDices', []))
CLIENT_PACKETS.append(Packet('LoginNewChar', [
    ('UserName', TYPE_UNICODE_STRING), 
    ('Password', TYPE_UNICODE_STRING),
    ('VerA', TYPE_I8),
    ('VerB', TYPE_I8),
    ('VerC', TYPE_I8),
    ('Race', TYPE_I8),
    ('Gender', TYPE_I8),
    ('Class', TYPE_I8),
    ('Head', TYPE_I16),
    ('Mail', TYPE_UNICODE_STRING),
    ('Homeland', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('Talk', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('Yell', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('Whisper', [
    ('TargetName', TYPE_UNICODE_STRING),
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('Walk', [
    ('Heading', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('RequestPositionUpdate', []))
CLIENT_PACKETS.append(Packet('Attack', []))
CLIENT_PACKETS.append(Packet('PickUp', []))
CLIENT_PACKETS.append(Packet('SafeToggle', []))
CLIENT_PACKETS.append(Packet('ResuscitationSafeToggle', []))
CLIENT_PACKETS.append(Packet('RequestGuildLeaderInfo', []))
CLIENT_PACKETS.append(Packet('RequestAtributes', []))
CLIENT_PACKETS.append(Packet('RequestFame', []))
CLIENT_PACKETS.append(Packet('RequestSkills', []))
CLIENT_PACKETS.append(Packet('RequestMiniStats', []))
CLIENT_PACKETS.append(Packet('CommerceEnd', []))
CLIENT_PACKETS.append(Packet('UserCommerceEnd', []))
CLIENT_PACKETS.append(Packet('UserCommerceConfirm', []))
CLIENT_PACKETS.append(Packet('CommerceChat', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('BankEnd', []))
CLIENT_PACKETS.append(Packet('UserCommerceOk', []))
CLIENT_PACKETS.append(Packet('UserCommerceReject', []))
CLIENT_PACKETS.append(Packet('Drop', [
    ('Slot', TYPE_I8),
    ('Amount', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('CastSpell', [
    ('Spell', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('LeftClick', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('DoubleClick', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('Work', [
    ('Skill', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('UseSpellMacro', []))
CLIENT_PACKETS.append(Packet('UseItem', [
    ('Slot', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('CraftBlacksmith', [
    ('Item', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('CraftCarpenter', [
    ('Item', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('WorkLeftClick', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ('Skill', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('CreateNewGuild', [
    ('Desc', TYPE_UNICODE_STRING),
    ('GuildName', TYPE_UNICODE_STRING),
    ('Site', TYPE_UNICODE_STRING),
    ('Codex', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('SpellInfo', [
    ('Slot', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('EquipItem', [
    ('Slot', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('ChangeHeading', [
    ('Heading', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('ModifySkills', [
    ('Skills', TYPE_I8 | TYPE_ARRAY, NUMSKILLS),
    ]))
CLIENT_PACKETS.append(Packet('Train', [
    ('PetIndex', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('CommerceBuy', [
    ('Slot', TYPE_I8),
    ('Amount', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('BankExtractItem', [
    ('Slot', TYPE_I8),
    ('Amount', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('CommerceSell', [
    ('Slot', TYPE_I8),
    ('Amount', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('BankDeposit', [
    ('Slot', TYPE_I8),
    ('Amount', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('ForumPost', [
    ('MsgType', TYPE_I8),
    ('Title', TYPE_UNICODE_STRING),
    ('Post', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('MoveSpell', [
    ('Direction', TYPE_BOOL),
    ('Slot', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('MoveBank', [
    ('Direction', TYPE_BOOL),
    ('Slot', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('ClanCodexUpdate', [
    ('Desc', TYPE_UNICODE_STRING),
    ('Codex', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('UserCommerceOffer', [
    ('Slot', TYPE_I8),
    ('Amount', TYPE_I32),
    ('OfferSlot', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('GuildAcceptPeace', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildRejectAlliance', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildRejectPeace', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildAcceptAlliance', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildOfferPeace', [
    ('Guild', TYPE_UNICODE_STRING),
    ('Proposal', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildOfferAlliance', [
    ('Guild', TYPE_UNICODE_STRING),
    ('Proposal', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildAllianceDetails', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildPeaceDetails', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildRequestJoinerInfo', [
    ('User', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildAlliancePropList', []))
CLIENT_PACKETS.append(Packet('GuildPeacePropList', []))
CLIENT_PACKETS.append(Packet('GuildDeclareWar', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildNewWebsite', [
    ('Website', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildAcceptNewMember', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildRejectNewMember', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildKickMember', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildUpdateNews', [
    ('News', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildMemberInfo', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildOpenElections', []))
CLIENT_PACKETS.append(Packet('GuildRequestMembership', [
    ('Guild', TYPE_UNICODE_STRING),
    ('Application', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildRequestDetails', [
    ('Guild', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('Online', []))
CLIENT_PACKETS.append(Packet('Quit', []))
CLIENT_PACKETS.append(Packet('GuildLeave', []))
CLIENT_PACKETS.append(Packet('RequestAccountState', []))
CLIENT_PACKETS.append(Packet('PetStand', []))
CLIENT_PACKETS.append(Packet('PetFollow', []))
CLIENT_PACKETS.append(Packet('ReleasePet', []))
CLIENT_PACKETS.append(Packet('TrainList', []))
CLIENT_PACKETS.append(Packet('Rest', []))
CLIENT_PACKETS.append(Packet('Meditate', []))
CLIENT_PACKETS.append(Packet('Resucitate', []))
CLIENT_PACKETS.append(Packet('Heal', []))
CLIENT_PACKETS.append(Packet('Help', []))
CLIENT_PACKETS.append(Packet('RequestStats', []))
CLIENT_PACKETS.append(Packet('CommerceStart', []))
CLIENT_PACKETS.append(Packet('BankStart', []))
CLIENT_PACKETS.append(Packet('Enlist', []))
CLIENT_PACKETS.append(Packet('Information', []))
CLIENT_PACKETS.append(Packet('Reward', []))
CLIENT_PACKETS.append(Packet('RequestMOTD', []))
CLIENT_PACKETS.append(Packet('UpTime', []))
CLIENT_PACKETS.append(Packet('PartyLeave', []))
CLIENT_PACKETS.append(Packet('PartyCreate', []))
CLIENT_PACKETS.append(Packet('PartyJoin', []))
CLIENT_PACKETS.append(Packet('Inquiry', []))
CLIENT_PACKETS.append(Packet('GuildMessage', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('PartyMessage', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('CentinelReport', [
    ('Code', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('GuildOnline', []))
CLIENT_PACKETS.append(Packet('PartyOnline', []))
CLIENT_PACKETS.append(Packet('CouncilMessage', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('RoleMasterRequest', [
    ('Request', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GMRequest', []))
CLIENT_PACKETS.append(Packet('BugReport', [
    ('Report', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('ChangeDescription', [
    ('Description', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildVote', [
    ('Vote', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('Punishments', [
    ('Name', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('ChangePassword', [
    ('OldPass', TYPE_UNICODE_STRING),
    ('NewPass', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('Gamble', [
    ('Amount', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('InquiryVote', [
    ('Opt', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('LeaveFaction', []))
CLIENT_PACKETS.append(Packet('BankExtractGold', [
    ('Amount', TYPE_I32),
    ]))
CLIENT_PACKETS.append(Packet('BankDepositGold', [
    ('Amount', TYPE_I32),
    ]))
CLIENT_PACKETS.append(Packet('Denounce', [
    ('Text', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('GuildFundate', []))
CLIENT_PACKETS.append(Packet('GuildFundation', [
    ('ClanType', TYPE_I8),
    ]))
CLIENT_PACKETS.append(Packet('PartyKick', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('PartySetLeader', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('PartyAcceptMember', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_PACKETS.append(Packet('Ping', []))
CLIENT_PACKETS.append(Packet('RequestPartyForm', []))
CLIENT_PACKETS.append(Packet('ItemUpgrade', [
    ('ItemIndex', TYPE_I16),
    ]))
CLIENT_PACKETS.append(PacketGMHeader('GMCommands', [
    # ('Command', TYPE_),
    ]))
CLIENT_PACKETS.append(Packet('InitCrafting', [
    ('TotalItems', TYPE_I32),
    ('ItemsPorCiclo', TYPE_I16),
    ]))
CLIENT_PACKETS.append(Packet('Home', []))
CLIENT_PACKETS.append(Packet('ShowGuildNews', []))
CLIENT_PACKETS.append(Packet('ShareNpc', []))
CLIENT_PACKETS.append(Packet('StopSharingNpc', []))
CLIENT_PACKETS.append(Packet('Consultation', []))
CLIENT_PACKETS.append(Packet('MoveItem', [
    ('OldSlot', TYPE_I8),
    ('NewSlot', TYPE_I8),
    ]))

# GM Packets
CLIENT_GM_PACKETS.append(None) # 0 is ignored.
CLIENT_GM_PACKETS.append(PacketGMCommand('GMMessage', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ShowName', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('OnlineRoyalArmy', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('OnlineChaosLegion', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('GoNearby', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Comment', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ServerTime', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('Where', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('CreaturesInMap', [
    ('Map', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('WarpMeToTarget', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('WarpChar', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Map', TYPE_I16),
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Silence', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SOSShowList', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('SOSRemove', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('GoToChar', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Invisible', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('GMPanel', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestUserList', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('Working', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('Hiding', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('Jail', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ('JailTime', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('KillNPC', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('WarnUser', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('EditChar', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Opcion', TYPE_I8),
    ('Arg1', TYPE_UNICODE_STRING),
    ('Arg2', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestCharInfo', [
    ('TargetName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestCharStats', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestCharGold', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestCharInventory', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestCharBank', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestCharSkills', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ReviveChar', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('OnlineGM', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('OnlineMap', [
    ('Map', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Forgive', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Kick', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Execute', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('BanChar', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('UnbanChar', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('NPCFollow', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('SummonChar', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SpawnListRequest', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('SpawnCreature', [
    ('NPC', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ResetNPCInventory', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('CleanWorld', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ServerMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('NickToIP', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('IPToNick', [
    ('A', TYPE_I8),
    ('B', TYPE_I8),
    ('C', TYPE_I8),
    ('D', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('GuildOnlineMembers', [
    ('GuildName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('TeleportCreate', [
    ('Map', TYPE_I16),
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ('Radio', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('TeleportDestroy', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('RainToggle', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('SetCharDescription', [
    ('Description', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ForceMIDIToMap', [
    ('MidiID', TYPE_I8),
    ('Map', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ForceWAVEToMap', [
    ('Wave', TYPE_I8),
    ('Map', TYPE_I16),
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RoyalArmyMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChaosLegionMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('CitizenMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('CriminalMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('TalkAsNPC', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('DestroyAllItemsInArea', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('AcceptRoyalCouncilMember', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('AcceptChaosCouncilMember', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ItemsInTheFloor', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('MakeDumb', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('MakeDumbNoMore', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('DumpIPTables', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('CouncilKick', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SetTrigger', [
    ('Trigger', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('AskTrigger', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('BannedIPList', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('BannedIPReload', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('GuildMemberList', [
    ('GuildName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('GuildBan', [
    ('GuildName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('BanIP', [ # FIXME: WRONG PACKET
    ('IP', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('UnbanIP', [
    ('IP', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('CreateItem', [
    ('Item', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('DestroyItems', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChaosLegionKick', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RoyalArmyKick', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ForceMIDIAll', [
    ('MidiID', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ForceWAVEAll', [
    ('WaveID', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RemovePunishment', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Punishment', TYPE_I8),
    ('NewText', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('TileBlockedToggle', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('KillNPCNoRespawn', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('KillAllNearbyNPCs', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('LastIP', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMOTD', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('SetMOTD', [
    ('Motd', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SystemMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('CreateNPC', [
    ('NpcIndex', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('CreateNPCWithRespawn', [
    ('NpcIndex', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ImperialArmour', [
    ('Index', TYPE_I8),
    ('ObjIndex', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChaosArmour', [
    ('Index', TYPE_I8),
    ('ObjIndex', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('NavigateToggle', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ServerOpenToUsersToggle', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('TurnOffServer', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('TurnCriminal', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ResetFactions', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RemoveCharFromGuild', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RequestCharMail', [
    ('UserName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('AlterPassword', [
    ('UserName', TYPE_UNICODE_STRING),
    ('CopyFrom', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('AlterMail', [
    ('UserName', TYPE_UNICODE_STRING),
    ('NewMail', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('AlterName', [
    ('UserName', TYPE_UNICODE_STRING),
    ('NewName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ToggleCentinelActivated', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('DoBackUp', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ShowGuildMessages', [
    ('GuildName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SaveMap', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoPK', [
    ('Pk', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoBackup', [
    ('Backup', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoRestricted', [
    ('RestrictedTo', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoNoMagic', [
    ('NoMagic', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoNoInvi', [
    ('NoInvi', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoNoResu', [
    ('NoResu', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoLand', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoZone', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoStealNpc', [
    ('RoboNpc', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoNoOcultar', [
    ('NoOcultar', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChangeMapInfoNoInvocar', [
    ('NoInvocar', TYPE_BOOL),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SaveChars', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('CleanSOS', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ShowServerForm', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('Night', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('KickAllChars', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ReloadNPCs', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ReloadServerIni', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ReloadSpells', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ReloadObjects', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('Restart', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ResetAutoUpdate', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ChatColor', [
    ('R', TYPE_I8),
    ('G', TYPE_I8),
    ('B', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Ignored', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('CheckSlot', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Slot', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SetIniVar', [
    ('Seccion', TYPE_UNICODE_STRING),
    ('Clave', TYPE_UNICODE_STRING),
    ('Valor', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('CreatePretorianClan', [
    ('Map', TYPE_I16),
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RemovePretorianClan', [
    ('Map', TYPE_I16),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('EnableDenounces', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('ShowDenouncesList', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('MapMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('SetDialog', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('Impersonate', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('Imitate', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('RecordAdd', [
    ('UserName', TYPE_UNICODE_STRING),
    ('Reason', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RecordRemove', [
    ('Index', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RecordAddObs', [
    ('Index', TYPE_I8),
    ('Obs', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('RecordListRequest', []))
CLIENT_GM_PACKETS.append(PacketGMCommand('RecordDetailsRequest', [
    ('Index', TYPE_I8),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('AlterGuildName', [
    ('OldGuildName', TYPE_UNICODE_STRING),
    ('NewGuildName', TYPE_UNICODE_STRING),
    ]))
CLIENT_GM_PACKETS.append(PacketGMCommand('HigherAdminsMessage', [
    ('Message', TYPE_UNICODE_STRING),
    ]))

# Server Packets

SERVER_PACKETS.append(Packet('Logged', [
    ('Clase', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('RemoveDialogs', []))
SERVER_PACKETS.append(Packet('RemoveCharDialog', [
    ('CharIndex', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('NavigateToggle', []))
SERVER_PACKETS.append(Packet('Disconnect', []))
SERVER_PACKETS.append(Packet('CommerceEnd', []))
SERVER_PACKETS.append(Packet('BankEnd', []))
SERVER_PACKETS.append(Packet('CommerceInit', []))
SERVER_PACKETS.append(Packet('BankInit', [
    ('Banco', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('UserCommerceInit', [
    ('DestUserName', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('UserCommerceEnd', []))
SERVER_PACKETS.append(Packet('UserOfferConfirm', []))
SERVER_PACKETS.append(Packet('CommerceChat', [
    ('Chat', TYPE_UNICODE_STRING),
    ('FontIndex', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('ShowBlacksmithForm', []))
SERVER_PACKETS.append(Packet('ShowCarpenterForm', []))
SERVER_PACKETS.append(Packet('UpdateSta', [
    ('Value', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('UpdateMana', [
    ('Value', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('UpdateHP', [
    ('Value', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('UpdateGold', [
    ('Value', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('UpdateBankGold', [
    ('Value', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('UpdateExp', [
    ('Value', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('ChangeMap', [
    ('Map', TYPE_I16),
    ('Version', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('PosUpdate', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('ChatOverHead', [
    ('Chat', TYPE_UNICODE_STRING),
    ('CharIndex', TYPE_I16),
    ('R', TYPE_I8),
    ('G', TYPE_I8),
    ('B', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('ConsoleMsg', [
    ('Chat', TYPE_UNICODE_STRING),
    ('FontIndex', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('GuildChat', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowMessageBox', [
    ('Chat', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('UserIndexInServer', [
    ('UserIndex', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('UserCharIndexInServer', [
    ('CharIndex', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('CharacterCreate', [
    ('CharIndex', TYPE_I16),
    ('Body', TYPE_I16),
    ('Head', TYPE_I16),
    ('Heading', TYPE_I8),
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ('Weapon', TYPE_I16),
    ('Shield', TYPE_I16),
    ('Helmet', TYPE_I16),
    ('FX', TYPE_I16),
    ('FXLoops', TYPE_I16),
    ('Name', TYPE_UNICODE_STRING),
    ('NickColor', TYPE_I8),
    ('Privileges', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('CharacterRemove', [
    ('CharIndex', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('CharacterChangeNick', [
    ('CharIndex', TYPE_I16),
    ('NewName', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('CharacterMove', [
    ('CharIndex', TYPE_I16),
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('ForceCharMove', [
    ('Direction', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('CharacterChange', [
    ('CharIndex', TYPE_I16),
    ('Body', TYPE_I16),
    ('Head', TYPE_I16),
    ('Heading', TYPE_I8),
    ('Weapon', TYPE_I16),
    ('Shield', TYPE_I16),
    ('Helmet', TYPE_I16),
    ('FX', TYPE_I16),
    ('FXLoops', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('ObjectCreate', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ('GrhIndex', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('ObjectDelete', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('BlockPosition', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ('Blocked', TYPE_BOOL),
    ]))
SERVER_PACKETS.append(Packet('PlayMidi', [
    ('MidiID', TYPE_I16),
    ('Loops', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('PlayWave', [
    ('WaveID', TYPE_I8),
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('GuildList', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('AreaChanged', [
    ('X', TYPE_I8),
    ('Y', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('PauseToggle', []))
SERVER_PACKETS.append(Packet('RainToggle', []))
SERVER_PACKETS.append(Packet('CreateFX', [
    ('CharIndex', TYPE_I16),
    ('FX', TYPE_I16),
    ('FXLoops', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('UpdateUserStats', [
    ('MaxHp', TYPE_I16),
    ('MinHp', TYPE_I16),
    ('MaxMan', TYPE_I16),
    ('MinMan', TYPE_I16),
    ('MaxSta', TYPE_I16),
    ('MinSta', TYPE_I16),
    ('Gld', TYPE_I32),
    ('Elv', TYPE_I8),
    ('Elu', TYPE_I32),
    ('Exp', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('WorkRequestTarget', [
    ('Skill', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('ChangeInventorySlot', [
    ('Slot', TYPE_I8),
    ('ObjIndex', TYPE_I16),
    ('ObjName', TYPE_UNICODE_STRING),
    ('Amount', TYPE_I16),
    ('Equiped', TYPE_BOOL),
    ('GrhIndex', TYPE_I16),
    ('ObjType', TYPE_I8),
    ('MaxHit', TYPE_I16),
    ('MinHit', TYPE_I16),
    ('MaxDef', TYPE_I16),
    ('MinDef', TYPE_I16),
    ('ObjSalePrice', TYPE_SINGLE),
    ]))
SERVER_PACKETS.append(Packet('ChangeBankSlot', [
    ('Slot', TYPE_I8),
    ('ObjIndex', TYPE_I16),
    ('ObjName', TYPE_UNICODE_STRING),
    ('Amount', TYPE_I16),
    ('GrhIndex', TYPE_I16),
    ('ObjType', TYPE_I8),
    ('MaxHit', TYPE_I16),
    ('MinHit', TYPE_I16),
    ('MaxDef', TYPE_I16),
    ('MinDef', TYPE_I16),
    ('ObjSalePrice', TYPE_SINGLE),
    ]))
SERVER_PACKETS.append(Packet('ChangeSpellSlot', [
    ('Slot', TYPE_I8),
    ('SpellID', TYPE_I16),
    ('Name', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('Atributes', [
    ('Fuerza', TYPE_I8),
    ('Agilidad', TYPE_I8),
    ('Inteligencia', TYPE_I8),
    ('Carisma', TYPE_I8),
    ('Constitucion', TYPE_I8),
    ]))
SERVER_PACKETS.append(PacketWithCount('BlacksmithWeapons', [
    ('Name', TYPE_UNICODE_STRING),
    ('GrhIndex', TYPE_I16),
    ('LingH', TYPE_I16),
    ('LingP', TYPE_I16),
    ('LingO', TYPE_I16),
    ('ArmasHerreroIndex', TYPE_I16),
    ('ObjUpgrade', TYPE_I16),
    ], TYPE_I16))
SERVER_PACKETS.append(PacketWithCount('BlacksmithArmors', [
    ('Name', TYPE_UNICODE_STRING),
    ('GrhIndex', TYPE_I16),
    ('LingH', TYPE_I16),
    ('LingP', TYPE_I16),
    ('LingO', TYPE_I16),
    ('ArmasHerreroIndex', TYPE_I16),
    ('ObjUpgrade', TYPE_I16),
    ], TYPE_I16))
SERVER_PACKETS.append(PacketWithCount('CarpenterObjects', [
    ('Name', TYPE_UNICODE_STRING),
    ('GrhIndex', TYPE_I16),
    ('Madera', TYPE_I16),
    ('MaderaElfica', TYPE_I16),
    ('ObjCarpinteroIndex', TYPE_I16),
    ('ObjUpgrade', TYPE_I16),
    ], TYPE_I16))
SERVER_PACKETS.append(Packet('RestOK', []))
SERVER_PACKETS.append(Packet('ErrorMsg', [
    ('Message', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('Blind', []))
SERVER_PACKETS.append(Packet('Dumb', []))
SERVER_PACKETS.append(Packet('ShowSignal', [
    ('Texto', TYPE_UNICODE_STRING),
    ('Grh', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('ChangeNPCInventorySlot', [
    ('Slot', TYPE_I8),
    ('ObjName', TYPE_UNICODE_STRING),
    ('Amount', TYPE_I16),
    ('Price', TYPE_SINGLE),
    ('GrhIndex', TYPE_I16),
    ('ObjIndex', TYPE_I16),
    ('ObjType', TYPE_I8),
    ('MaxHit', TYPE_I16),
    ('MinHit', TYPE_I16),
    ('MaxDef', TYPE_I16),
    ('MinDef', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('UpdateHungerAndThirst', [
    ('MaxAgu', TYPE_I8),
    ('MinAgu', TYPE_I8),
    ('MaxHam', TYPE_I8),
    ('MinHam', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('Fame', [
    ('Asesino', TYPE_I32),
    ('Bandido', TYPE_I32),
    ('Burgues', TYPE_I32),
    ('Ladron', TYPE_I32),
    ('Noble', TYPE_I32),
    ('Plebe', TYPE_I32),
    ('Promedio', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('MiniStats', [
    ('CiudadanosMatados', TYPE_I32),
    ('CriminalesMatados', TYPE_I32),
    ('UsuariosMatados', TYPE_I32),
    ('NpcsMuertos', TYPE_I16),
    ('Clase', TYPE_I8),
    ('Pena', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('LevelUp', [
    ('SkillPoints', TYPE_I16),
    ]))
SERVER_PACKETS.append(Packet('AddForumMsg', [
    ('ForumType', TYPE_I32),
    ('Title', TYPE_UNICODE_STRING),
    ('Author', TYPE_UNICODE_STRING),
    ('Message', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowForumForm', [
    ('Visibilidad', TYPE_I8),
    ('CanMakeSticky', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('SetInvisible', [
    ('charIndex', TYPE_I16),
    ('invisible', TYPE_BOOL),
    ]))
SERVER_PACKETS.append(Packet('DiceRoll', [
    ('Fuerza', TYPE_I8),
    ('Agilidad', TYPE_I8),
    ('Inteligencia', TYPE_I8),
    ('Carisma', TYPE_I8),
    ('Constitucion', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('MeditateToggle', []))
SERVER_PACKETS.append(Packet('BlindNoMore', []))
SERVER_PACKETS.append(Packet('DumbNoMore', []))
SERVER_PACKETS.append(Packet('SendSkills', [
    ('Skills', TYPE_I8 | TYPE_ARRAY, NUMSKILLS * 2),
    ]))
SERVER_PACKETS.append(Packet('TrainerCreatureList', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('GuildNews', [
    ('News', TYPE_UNICODE_STRING),
    ('EnemiesList', TYPE_UNICODE_STRING),
    ('AlliesList', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('OfferDetails', [
    ('Details', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('AlianceProposalsList', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('PeaceProposalsList', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('CharacterInfo', [
    ('CharName', TYPE_UNICODE_STRING),
    ('Race', TYPE_I8),
    ('Class', TYPE_I8),
    ('Gender', TYPE_I8),
    ('Level', TYPE_I8),
    ('Gold', TYPE_I32),
    ('Bank', TYPE_I32),
    ('Reputation', TYPE_I32),
    ('PreviousPetitions', TYPE_UNICODE_STRING),
    ('CurrentGuild', TYPE_UNICODE_STRING),
    ('PreviousGuilds', TYPE_UNICODE_STRING),
    ('RoyalArmy', TYPE_BOOL),
    ('ChaosLegion', TYPE_BOOL),
    ('CiudadanosMatados', TYPE_I32),
    ('CriminalesMatados', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('GuildLeaderInfo', [
    ('GuildList', TYPE_UNICODE_STRING),
    ('MemberList', TYPE_UNICODE_STRING),
    ('GuildNews', TYPE_UNICODE_STRING),
    ('JoinRequests', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('GuildMemberInfo', [
    ('GuildList', TYPE_UNICODE_STRING),
    ('MemberList', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('GuildDetails', [
    ('GuildName', TYPE_UNICODE_STRING),
    ('Founder', TYPE_UNICODE_STRING),
    ('FoundationDate', TYPE_UNICODE_STRING),
    ('Leader', TYPE_UNICODE_STRING),
    ('URL', TYPE_UNICODE_STRING),
    ('MemberCount', TYPE_I16),
    ('ElectionsOpen', TYPE_BOOL),
    ('Aligment', TYPE_UNICODE_STRING),
    ('EnemiesCount', TYPE_I16),
    ('AlliesCount', TYPE_I16),
    ('AntifactionPoints', TYPE_UNICODE_STRING),
    ('Codex', TYPE_UNICODE_STRING),
    ('GuildDesc', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowGuildFundationForm', []))
SERVER_PACKETS.append(Packet('ParalizeOK', []))
SERVER_PACKETS.append(Packet('ShowUserRequest', [
    ('Details', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('TradeOK', []))
SERVER_PACKETS.append(Packet('BankOK', []))
SERVER_PACKETS.append(Packet('ChangeUserTradeSlot', [
    ('OfferSlot', TYPE_I8),
    ('ObjIndex', TYPE_I16),
    ('Amount', TYPE_I32),
    ('GrhIndex', TYPE_I16),
    ('ObjType', TYPE_I8),
    ('MaxHit', TYPE_I16),
    ('MinHit', TYPE_I16),
    ('MaxDef', TYPE_I16),
    ('MinDef', TYPE_I16),
    ('Price', TYPE_I32),
    ('ObjName', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('SendNight', [
    ('Night', TYPE_BOOL),
    ]))
SERVER_PACKETS.append(Packet('Pong', []))
SERVER_PACKETS.append(Packet('UpdateTagAndStatus', [
    ('CharIndex', TYPE_I16),
    ('NickColor', TYPE_I8),
    ('Tag', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('SpawnList', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowSOSForm', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowMOTDEditionForm', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowGMPanelForm', []))
SERVER_PACKETS.append(Packet('UserNameList', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowDenounces', [
    ('Data', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(PacketWithCount('RecordList', [
    ('Usuario', TYPE_UNICODE_STRING),
    ], TYPE_I8))
SERVER_PACKETS.append(Packet('RecordDetails', [
    ('Creador', TYPE_UNICODE_STRING),
    ('Motivo', TYPE_UNICODE_STRING),
    ('Online', TYPE_BOOL),
    ('IP', TYPE_UNICODE_STRING),
    ('OnlineTime', TYPE_UNICODE_STRING),
    ('Obs', TYPE_UNICODE_STRING),
    ]))
SERVER_PACKETS.append(Packet('ShowGuildAlign', []))
SERVER_PACKETS.append(Packet('ShowPartyForm', [
    ('EsLider', TYPE_I8),
    ('Data', TYPE_UNICODE_STRING),        
    ('Exp', TYPE_I32),
    ]))
SERVER_PACKETS.append(Packet('UpdateStrenghtAndDexterity', [
    ('Fuerza', TYPE_I8),
    ('Agilidad', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('UpdateStrenght', [
    ('Fuerza', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('UpdateDexterity', [
    ('Agilidad', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('AddSlots', [
    ('Mochila', TYPE_I8),
    ]))
SERVER_PACKETS.append(Packet('MultiMessage', [])) # FIXME
SERVER_PACKETS.append(Packet('StopWorking', []))
SERVER_PACKETS.append(Packet('CancelOfferItem', [
    ('Slot', TYPE_I8),
    ]))
