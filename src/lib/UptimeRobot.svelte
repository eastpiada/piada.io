<script>
	let getPoolUptime = (async () => {
		const res = await fetch(
			'https://api.uptimerobot.com/v2/getMonitors?format=json&api_key=ur1967275-b3b281dc8596ed10791ab890', { method: 'POST' }
		);
		return await res.json();
	})();
</script>

<div class="w3-container w3-black" style="padding:128px 16px" id="about">
    <div class="w3-row-padding w3-center" style="margin-top:84px!important">
        {#await getPoolUptime}
        <div class="w3-center w3-padding-32">
            <p class="w3-large">Loading Relay Statuses</p>
        </div>
        {:then data}
            {#if data.stat === "ok"}
                {#if data.monitors[0].status === 2}
                <div class="w3-third w3-padding-32">
                    <i class="fa-solid fa-heart-circle-check fa-beat-fade w3-margin-bottom w3-jumbo w3-text-green" style="--fa-animation-duration: 2s; --fa-beat-fade-opacity: 0.67; --fa-beat-fade-scale: 1.055;"></i>
                    <p class="w3-large">Relay 1 is doing just fine</p>
                </div>
                {:else}
                <div class="w3-third w3-padding-32">
                    <i class="fa-solid fa-heart-crack w3-margin-bottom w3-jumbo w3-text-red"></i>
                    <p class="w3-large">Relay 1 is not responding</p>
                </div>
                {/if}
                <div class="w3-third w3-padding-32">
                    <i class="fa-solid fa-circle w3-margin-bottom w3-tiny w3-text-green"></i><span class="w3-xlarge" style="padding-left:5px;"><a href="https://stats.uptimerobot.com/lgx2rF184V" rel="no-referrer" target="_blank">UptimeRobot</a></span>
                </div>
                {#if data.monitors[1].status === 2}
                <div class="w3-third w3-padding-32">
                    <i class="fa-solid fa-heart-circle-check fa-beat-fade w3-margin-bottom w3-jumbo w3-text-green"></i>
                    <p class="w3-large">Relay 2 is doing just fine</p>
                </div>
                {:else}
                <div class="w3-third w3-padding-32">
                    <i class="fa-solid fa-heart-crack w3-margin-bottom w3-jumbo w3-text-red"></i>
                    <p class="w3-large">Relay 2 is not responding</p>
                </div>
                {/if}
            {:else}
            <div class="w3-center w3-padding-32">
                <p class="w3-large">No UptimeRobot API Available</p>
            </div>
            {/if}
        {:catch error}
        <div class="w3-center w3-padding-32">
            <p class="w3-large">No UptimeRobot API Available</p>
        </div>
        {/await}
    </div>
</div>