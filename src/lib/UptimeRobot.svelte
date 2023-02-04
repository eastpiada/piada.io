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
        <span>Loading Pool Relay Statuses...</span>
        {:then data}
        <span>{data.stat}</span>
        {:catch error}
        <span>API Error</span>
        {/await}
    </div>
</div>

<style>
    iframe { width: 100%; height: 800px; }
</style>