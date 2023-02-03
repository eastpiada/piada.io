
<script>
	import Delegate from "$lib/Delegate.svelte";

  let aaShip = "/images/ship-420.png";
</script>

<header class="rimage w3-display-container" id="home">
    <div class="w3-display-left w3-text-white" style="padding:48px">
      <h1 class="w3-jumbo w3-hide-small">Stake with PIADA</h1>
      <h1 class="w3-xxlarge w3-hide-large w3-hide-medium">Stake with PIADA</h1>
      <h4 class="w3-xlarge">
        Armada Alliance OGs forging Cardano blockchain rewards<br />on efficient hardware since mainnet epoch 255
      </h4>
      <Delegate/>
    </div>
    <div class="w3-display-bottomleft w3-xlarge w3-section w3-text-white" style="padding:24px 48px">
      <!--<span class="p-p3">{@html cardanoLogoSvg}</span>-->
      <span class="p-p3">&#960; &#43; &#8371; &#61; &#8766;</span>
      <a href="https://twitter.com/Piada_stakePool" rel="noreferrer" target="_blank"><i class="fa-brands fa-twitter w3-hover-opacity p-p3"></i></a>
      <a href="https://t.me/piadapool" rel="noreferrer" target="_blank"><i class="fa-brands fa-telegram w3-hover-opacity p-p3"></i></a>
      <a href="https://armada-alliance.com/" rel="noreferrer" target="_blank"><img class="w3-hover-opacity" src={aaShip} alt="Armada Alliance Logo" style="height:30px;"></a>
    </div>
</header>

<style>
  h1,h4 {text-shadow:2px 2px 4px #000;}
  .rimage {
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-image: url('/images/3d-rendering-digital-binary-data-microchip-with-glow-circuit-board-background.jpg');
    min-height: 100%;
  }
</style>