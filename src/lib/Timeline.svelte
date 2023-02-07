<script>
    import {
		Timeline,
		TimelineItem,
		TimelineSeparator,
		TimelineDot,
		TimelineConnector,
		TimelineContent,
		TimelineOppositeContent
	} from 'svelte-vertical-timeline';
    import storyData from '$lib/data/storyData.json';
</script>

<div class="w3-container w3-black" style="padding:128px 2px" id="timeline">
    <Timeline position="alternate" style="margin-top:64px">
        {#each storyData as sd}
        <TimelineItem>
            <TimelineOppositeContent slot="opposite-content">
                <h4>{sd.date}</h4>
            </TimelineOppositeContent>
            <TimelineSeparator>
                <TimelineDot style={'width: 45px; height: 48px; background-color: #fff; display: flex; justify-content: center; border-color: transparent;'}>
                    <i class="fa-solid {sd.faIcon} fa-beat-fade w3-margin-bottom w3-xxlarge" style="--fa-animation-duration: 2s; --fa-beat-fade-opacity: 0.67; --fa-beat-fade-scale: 1.055; {sd.faStyle}"></i>
                </TimelineDot>
                <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent style={'line-height:1.6em;margin-bottom:60px;'}>
                {#if sd.url != ""}
                <h3><a href={sd.url} rel="noreferrer" target="_blank">{sd.title}</a></h3>
                {:else}
                <h3>{sd.title}</h3>
                {/if}
                <p class="w3-large">{sd.details}</p>
            </TimelineContent>
        </TimelineItem>
        {/each}
    </Timeline>
</div>