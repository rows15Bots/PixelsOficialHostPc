JSON.stringify([
    ...Array.from(Phaser.Display.Canvas.CanvasPool.pool[1].parent.scene.game.scene.scenes[1].otherPlayers.values())
      .filter(player => player.playerData.label === "avetruz")
      .map(player => [player.playerData.label, player.playerData.position]),
    ["Me:",Phaser.Display.Canvas.CanvasPool.pool[1].parent.scene.game.scene.scenes[1].selfPlayer.position]
  ])


ws = Phaser.Display.Canvas.CanvasPool.pool[0].parent.game.scene.scenes[1].camera.scene.stateManager.room.connection.transport.ws
ws = Phaser.Display.Canvas.CanvasPool.pool[0].parent.game.scene.scenes[1].stateManager.room.connection.transport.ws

// (XY array)
var currentPos = game.scene.systemScene.scene.manager.scenes[1].selfPlayer.container; 
let xValue = currentPos.x;
let yValue = currentPos.y;
// Energy / Coin V1        
let energyBalanceElement = document.querySelector('span[class*="commons_coinBalance"][class*="Hud_energytext"]');
let energyBalanceText = energyBalanceElement ? energyBalanceElement.textContent.trim() : null;
let coinBalanceElement = document.querySelector('span[class*="commons_coinBalance"]');
let coinBalanceText = coinBalanceElement ? coinBalanceElement.textContent.trim() : null;
//Inventory (items and active row)
let activeRow = game.scene.keys[Object.keys(game.scene.keys)[1]].sys.data.scene.stateManager.selfPlayer.inventory.activeRow
let slots = 		[...game.scene.keys[Object.keys(game.scene.keys)[1]].sys.data.scene.stateManager.selfPlayer.inventory.slots.$items]
let slotValues = slots.map(([key, obj]) => [obj.slot,obj.item,obj.quantity])
let slotString = slotValues.join(',,,');
//Map Name
let sceneKeys = game.scene.keys;
let sceneKeysArray = sceneKeys ? Object.keys(sceneKeys) : [];
let firstSceneKey = sceneKeysArray.length > 1 ? sceneKeysArray[1] : null;
//7crops
game.scene.systemScene.scene.manager.scenes[1].crops
//1xy camera mid point (se colocar offset 1, a camera fica exatamente no player - game.scene.systemScene.scene.manager.scenes[1].camera.lerp)
game.scene.systemScene.scene.manager.scenes[1].camera.midPoint
//6coins
var slots1 = 		[...game.scene.scenes[1].stateManager.selfPlayer.coinInventory]
//vip
game.scene.systemScene.scene.manager.scenes[1].selfPlayer.characterHelper.characterData.kind
//Bookmarked Maps 
var slots1 = 		[...game.scene.scenes[1].stateManager.selfPlayer.bookmarks.bookmarkedMaps]
//levels
game.scene.scenes[1].stateManager.selfPlayer.levels
//Achievments
game.scene.scenes[1].stateManager.selfPlayer.achievements
//4quests
game.scene.scenes[1].stateManager.selfPlayer.quests
//5energy
game.scene.scenes[1].stateManager.selfPlayer.energy.level
//8mousePosIngame 
//sempre screenX
game.input.mousePointer.x 
//Pos hoverando = worldX / pos no chão = screenX
game.input.mousePointer.worldX
//Várias infos do mapa/conexão
game.scene.scenes[1].stateManager.room
game.scene.scenes[1].stateManager.room.hasJoined // Logado ou não (não existe se tiver ddeslogado)



//SOIL
temp
game.scene.game.scene.scenes[1].entities > começam com E
crop pos (center left)
current > 3a4

entityType
: 
"soil"

isCursor
: 
false

//Dialog ou Popup open



//dialog
<div class="RoomLayout_roomLayout__QU057"><div id="game-container" class="GameContainer_game-container__gT4TM" tabindex="-1"><canvas width="498" height="993" style="image-rendering: pixelated;"></canvas></div><div class="GameContainer_gameCover___mB2c" style="opacity: 0;"></div><div class="room-layout"><div class="UIContainer_uiContainer__k_NnG pixelfont"><div style="pointer-events: none; user-select: none; background: none; overflow: hidden; display: block; position: absolute; inset: 0px;"><div style="background: none; position: absolute; left: 0px; top: 0px; image-rendering: pixelated; width: 60.241%; height: 60.241%; transform-origin: 0px 0px 0px; transform: scale3d(1.66, 1.66, 1);"><div class="Hud_top__nZRRz Hud_left__mQoqW"><div class="Hud_topLeftBackground__OhgQS" style="background-image: url(&quot;https://d31ss916pli4td.cloudfront.net/game/ui/hud/purple/hud_corner_left.png&quot;);"><div class="Hud_berry__6A2FS"><div class="commons_balanceDisplay__NSs8e"><img class="commons_coin-icon__CtrwT" src="//d31ss916pli4td.cloudfront.net/uploadedAssets/currency/pixels_berry_currency_new.png" style="height: 12px; margin-right: 2px; margin-bottom: 0px;"><span class="commons_coinBalance__d9sah" style="font-size: 10px;">18.829</span></div></div><div class="Hud_pixelcoin__EUbKE"><div class="commons_balanceDisplay__NSs8e"><img class="commons_coin-icon__CtrwT" src="//d31ss916pli4td.cloudfront.net/uploadedAssets/currency/pixels_pixel_currency_new_2.png" style="height: 12px; margin-right: 2px; margin-bottom: 0px;"><span class="commons_coinBalance__d9sah" style="font-size: 10px;">0</span></div></div><div class="Hud_energy__67nU9"><div class="commons_balanceDisplay__NSs8e Hud_emptybar__O_4oe"><img class="commons_coin-icon__CtrwT" src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_icon_energy.png" style="height: 12px; margin-right: 2px; margin-bottom: 0px;"><span class="commons_coinBalance__d9sah Hud_energytext__3PQZQ" style="font-size: 10px;">32,79</span></div><div class="commons_balanceDisplay__NSs8e Hud_filledbar__lT290" style="width: 3.2787%;"><img class="commons_coin-icon__CtrwT" src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_icon_energy.png" style="height: 12px; margin-right: 2px; margin-bottom: 0px;"><span class="commons_coinBalance__d9sah Hud_energytext__3PQZQ" style="font-size: 10px;">32,79</span></div></div><button type="button" class="Hud_outside__zzIGQ" style="left: 90.695px; top: 2.58205px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_icon_land.png" aria-label="Land and Bookmarks" class=""></button><button type="button" class="Hud_outside__zzIGQ" style="left: 80.4467px; top: 34.123px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_temp_icon_skills.png" aria-label="Skills" class=""></button><button type="button" class="Hud_outside__zzIGQ" style="left: 60.9533px; top: 60.9533px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_icon_social.png" aria-label="Player" class=""></button><button type="button" class="Hud_outside__zzIGQ" style="left: 34.123px; top: 80.4467px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/PetButton.png" aria-label="Pets" class=""></button><button type="button" class="Hud_outside__zzIGQ" style="left: 2.58205px; top: 90.695px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_temp_icon_map.png" aria-label="Map View" class=""></button></div></div><div class="Hud_top__nZRRz Hud_right__QJpt5"><div class="Hud_topRightBackground__z4cEZ" style="background-image: url(&quot;https://d31ss916pli4td.cloudfront.net/game/ui/hud/purple/hud_corner_right.png&quot;);"><button type="button" class="Hud_quests__DaLW3"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_corner_right_note.png" aria-label="Quests" class=""><div class="Hud_questcount__MoHmh">2</div></button><button type="button" class="Hud_outside__zzIGQ" style="right: 90.695px; top: 2.58205px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/DashButton.png" aria-label="Dashboard" class=""></button><button type="button" class="Hud_outside__zzIGQ" style="right: 80.4467px; top: 34.123px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/SettingsButton.png" aria-label="Settings" class=""></button><button type="button" class="Hud_mailbox__qj4Ou Hud_outside__zzIGQ" style="right: 60.9533px; top: 60.9533px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_mail_button.png" aria-label="Mail" class=""></button><button type="button" class="Hud_outside__zzIGQ" style="right: 34.123px; top: 80.4467px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_temp_icon_questionmark.png" aria-label="Support" class=""></button><button type="button" class="Hud_outside__zzIGQ" style="right: 2.58205px; top: 90.695px; width: 28px; height: 28px;"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/hud_temp_icon_logout.png" aria-label="Log Out" class=""></button></div></div><div draggable="false" class="Hud_bottom__P9XWZ" style="height: 133px;"><button type="button" class="Hud_leftButton__1fv1P"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/chat.png" class=""></button><button type="button" class="Hud_rightButton__4AX4I"><img src="https://d31ss916pli4td.cloudfront.net/game/ui/hud/cycle.png" class=""></button><div class="Hud_slidingGroup__ZaO10" style="transform: translate3d(0px, 80px, 0px);"><button type="button" class="Hud_topButton__4Z5lK"><img class=""></button><div class="Hud_itemClip__Ph5Xx"><div class="Hud_itemList__PCP7A" style="transform: translate3d(0px, 0px, 0px); transition: transform 0.1s linear 0s;"><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">7</div><div class="clickable" style="height: 32px; width: 32px;"><img class="Hud_itemImage__TNSfp" src="blob:https://play.pixels.xyz/61ae395d-60a2-41b8-a9d0-b49916b04280" crossorigin="anonymous"></div><div class="Hud_quantity__V_YWQ"></div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">8</div><div class="clickable" style="height: 32px; width: 32px;"><img class="Hud_itemImage__TNSfp" src="blob:https://play.pixels.xyz/fd74afc0-c45e-4d53-97a5-dc18d42efdd7" crossorigin="anonymous"></div><div class="Hud_quantity__V_YWQ"></div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">9</div><div class="clickable" style="height: 32px; width: 32px;"><img class="Hud_itemImage__TNSfp" src="blob:https://play.pixels.xyz/966414c6-f5e7-4d7a-8d9b-a6591d0e7772" crossorigin="anonymous"></div><div class="Hud_quantity__V_YWQ">x267</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">10</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">11</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">12</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">13</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">14</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">15</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">16</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">17</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">18</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">1</div><div class="clickable" style="height: 32px; width: 32px;"><img class="Hud_itemImage__TNSfp" src="blob:https://play.pixels.xyz/825270fb-ebd3-4bd6-97ad-f959c58a0845" crossorigin="anonymous"></div><div class="Hud_quantity__V_YWQ">x308</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">2</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">3</div><div class="clickable" style="height: 32px; width: 32px;"><img class="Hud_itemImage__TNSfp" src="blob:https://play.pixels.xyz/5199924f-c2d1-4be9-b3fb-956cd526d330" crossorigin="anonymous"></div><div class="Hud_quantity__V_YWQ"></div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">4</div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">5</div><div class="clickable" style="height: 32px; width: 32px;"><img class="Hud_itemImage__TNSfp" src="blob:https://play.pixels.xyz/a2431308-e2d3-4648-937d-c6323dc98a3a" crossorigin="anonymous"></div><div class="Hud_quantity__V_YWQ"></div></div><div class="Hud_item__YGtIC"><div class="Hud_shortcut__UvE3h">6</div><div class="clickable" style="height: 32px; width: 32px;"><img class="Hud_itemImage__TNSfp" src="blob:https://play.pixels.xyz/28377a9b-4d54-4403-8fd0-88169efb2003" crossorigin="anonymous"></div><div class="Hud_quantity__V_YWQ"></div></div></div></div><div class="Hud_itemsTop__cYzyR"></div><div class="Hud_itemsRest___9h8b" style="height: 80px;"></div></div></div><div class="GameDialog_dialog5__ZBFqO"><div class="GameDialog_content__dE2Xj GameDialog_showVerticalBackground__HmFLs" style="background-image: url(&quot;/assets/ui/dialogue/dialog_background_portrait.png&quot;); transform: scale(calc(1));"><div class="GameDialog_messageBox___s2tN"><div class="GameDialog_message__4kY4E"><span>Hey there! I'm Priya, and I've landed this new gig here at the Post Office.</span><span style="opacity: 0;"></span></div></div><div class="GameDialog_avatar__bPdln"><div style="width: 33px; height: 50px; margin: 0px auto;"><div class="CharacterBuilder_piecesContainer__uIs3y" style="width: 100%; height: 100%;"><div style="width: 33px; height: 50px; overflow: hidden;"><div style="transform-origin: 0px 0px; transform: scale(1.04167); position: absolute; top: 0px; left: 0px;"><div class="pixelated Sprite_spriteAnimation32_0_5__ypJ4Z" style="width: 32px; height: 48px; background-image: url(&quot;blob:https://play.pixels.xyz/8c0a50a2-3cf2-4809-9196-e625bd332e9a&quot;); box-shadow: none;"></div></div></div><div style="width: 33px; height: 50px; overflow: hidden;"><div style="transform-origin: 0px 0px; transform: scale(1.04167); position: absolute; top: 0px; left: 0px;"><div class="pixelated Sprite_spriteAnimation32_0_5__ypJ4Z" style="width: 32px; height: 48px; background-image: url(&quot;blob:https://play.pixels.xyz/2c76c451-8ba0-4fdd-b0b4-4d3058e5b5b1&quot;); box-shadow: none;"></div></div></div><div style="width: 33px; height: 50px; overflow: hidden;"><div style="transform-origin: 0px 0px; transform: scale(1.04167); position: absolute; top: 0px; left: 0px;"><div class="pixelated Sprite_spriteAnimation32_0_5__ypJ4Z" style="width: 32px; height: 48px; background-image: url(&quot;blob:https://play.pixels.xyz/88c66ac4-3630-4e2e-9578-a3fa22673b41&quot;); box-shadow: none;"></div></div></div><div style="width: 33px; height: 50px; overflow: hidden;"><div style="transform-origin: 0px 0px; transform: scale(1.04167); position: absolute; top: 0px; left: 0px;"><div class="pixelated Sprite_spriteAnimation32_0_5__ypJ4Z" style="width: 32px; height: 48px; background-image: url(&quot;blob:https://play.pixels.xyz/6aa64d66-9b0a-45f1-9a51-980ca8c930fa&quot;); box-shadow: none;"></div></div></div><div style="width: 33px; height: 50px; overflow: hidden;"><div style="transform-origin: 0px 0px; transform: scale(1.04167); position: absolute; top: 0px; left: 0px;"><div class="pixelated Sprite_spriteAnimation32_0_5__ypJ4Z" style="width: 32px; height: 48px; background-image: url(&quot;blob:https://play.pixels.xyz/8c607706-a8c8-4024-aefb-faacf5caa6b2&quot;); box-shadow: none;"></div></div></div></div></div></div><div class="GameDialog_avatarname__elhuJ">Priya</div><div class="GameDialog_buttons__AIhXL"><button type="button" class="GameDialog_skip__Y5RGE"><img></button></div></div></div></div></div><div class="selecteditem" style="transform: translate3d(517px, 744px, 0px);"></div></div></div></div>

//X
<button type="button" class="InventoryWindow_closeBtn__ioczI"><img src=""></button>

//player tabindex

<div class="Profile_blurbg__VAn2q commons_uikit__Nmsxg"><button class="Profile_closeButton__1n0Um" type="button">✖

//travel
<div class="LandAndTravel_container__WCM6U commons_uikit__Nmsxg"><button type="button" class="commons_closeBtn__UobaL"></button><div class="LandAndTravel_header__irEHu"><div class="LandAndTravel_title__6WrMk">Land &amp; Travel</div></div><div class="LandAndTravel_title__6WrMk"></div><div class="LandAndTravel_customHeader__goUPo"><button type="button">Go to Terravilla</button></div><div class="LandAndTravel_tabs__L8FHU"><button class="LandAndTravel_tab__LD39V"><img src="/assets/landandtravel/land_inactive.png"></button><button class="LandAndTravel_tab__LD39V"><img src="/assets/landandtravel/house_active.png"></button><button class="LandAndTravel_tab__LD39V"><img src="/assets/landandtravel/bookmark_inactive.png"></button></div><div class="LandAndTravel_content__b_dal commons_scrollArea__dCnqw"><div class="LandAndTravel_subtitle__Uy4zk">My Land</div><div class="LandAndTravel_mapsSquare__vG99V"><div class="LandAndTravel_mapSquare__LuVEh"><div>My Speck</div><div><img src="/assets/landandtravel/land_green.png"></div><button type="button" class="LandAndTravel_buttonTeleport__Z6fS4">Go</button></div></div></div></div>












var currentPos = game.scene.systemScene.scene.manager.scenes[1].selfPlayer.container; 
















//Quero achar:
//2vip

// {
//     "vip": {
//         "expiration": 1709891595761
//     }
// }


//kind: "vip"
// textbg
// : 
// 16370533
// textcolor
// : 
// 9655068



// kind
// : 
// "normal"
// label
// : 
// "erinejljcik"
// textbg
// : 
// 15262975
// textcolor
// : 
// 2236484


// {
//     "avatar": {
//         "_id": "64ca74bb817596d50f82fe54",
//         "id": "players",
//         "kind": "avatar",
//         "enabled": false,
//         "createdAt": 1657145539397,
//         "animations": {
//             "idle": {

//     "label": "rows",
//     "modifiers": [],
//     "kind": "normal"
// }