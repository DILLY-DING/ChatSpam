function tpar(plrname)
    repeat wait() until game:IsLoaded()

    game:GetService("ReplicatedStorage"):WaitForChild("SetReplicationFocusOverride"):FireServer(false)

    local ts = game:GetService("TeleportService")
    local p = game:GetService("Players").LocalPlayer

    function tp(plrname)
        local player = game:GetService("Players").LocalPlayer
        local players = game:GetService("Players")
        local currpos = player.Character.HumanoidRootPart.Position
        local tagUtils = require(game:GetService("ReplicatedStorage").Tag.TagUtils)
        local workspace = game:GetService("Workspace")
        local target = game:GetService("Players"):FindFirstChild(plrname).Character:FindFirstChild("HumanoidRootPart")

        local function isQKeyPressed()
            return game:GetService("UserInputService"):IsKeyDown(Enum.KeyCode.Q)
        end
        
        
        
        


        function instanttp(plrname)
            player.Character.HumanoidRootPart.CFrame = players:FindFirstChild(plrname).Character.HumanoidRootPart.CFrame
        end

        function gravity(set)
            workspace.Gravity = tonumber(set) or 196.2
        end

        function ragdoll() 
            local oldIsPointInTag
            tagUtils.isPointInTag = function(point, tag)
                if tag == "NoRagdoll" or tag == "NoFallDamage" then 
                    return true
                end
                
                return oldIsPointInTag(point, tag)
            end
        end
        ragdoll()

        local part = player.Character:FindFirstChild("HumanoidRootPart")

        if not part then
            return
        end
        
        local y_level = 500
        local target_position = target.Position
        local higher_position = Vector3.new(target_position.X, y_level, target_position.Z)
        local speed = 150
        
        
        local function isConditionMet(currentPos, targetPos)
            return (currentPos - targetPos).Magnitude < 10
        end
        
        repeat
            local velocity_unit = (higher_position - part.Position).Unit * speed
            part.Velocity = Vector3.new(velocity_unit.X, 0, velocity_unit.Z)
            wait()
        
            part.CFrame = CFrame.new(part.Position.X, y_level, part.Position.Z)
        
            
            if isQKeyPressed() then
                break
            end
        until isConditionMet(part.Position, higher_position)
        
        part.CFrame = CFrame.new(part.Position.X, target_position.Y, part.Position.Z)
        part.Velocity = Vector3.new(0, 0, 0)
        
    end

    tp(plrname)

    while true do
        if game:GetService("Players").LocalPlayer.Folder:FindFirstChild("Cuffed") then
            queue_on_teleport('loadstring(game:HttpGet("https://raw.githubusercontent.com/DILLY-DING/Roblox-scripts/main/TPAR.lua"))()')
            ts:Teleport(game.PlaceId, p)
        end
        wait(0.1)
    end
end

print("Rejoined!!")
tpar("MRTOOGLE_A10")
