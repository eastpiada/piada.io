<script>
  import '../app.css';
	import Delegate from '$lib/Delegate.svelte';
  //let logoPic = "/images/piada-stake-pool-logo.png";
  let logoPic = "/images/raspberry-dots-small.png";
  let aaShip = "/images/ship-420.png";

  // Toggle between showing and hiding the sidebar when clicking the menu icon
  /**
	 * @type {HTMLElement}
	 */
  let piadaSidebar;

  function w3_open() {
    if (piadaSidebar.style.display === 'block') {
      piadaSidebar.style.display = 'none';
    } else {
      piadaSidebar.style.display = 'block';
    }
    return false;
  }

// Close the sidebar with the close button
  function w3_close() {
    piadaSidebar.style.display = "none";
    return false;
  }
</script>

<!-- Navbar (sit on top) -->
<div class="w3-top">
    <div class="w3-bar w3-black w3-card" id="piadaNavbar">
      <a href="#home" class="w3-bar-item"><img src={logoPic} alt="PIADA Logo" style="height:60px;"></a>
      <!-- Right-sided navbar links -->
      <div class="w3-right w3-hide-small">
        <a href="#about" class="w3-bar-item w3-button">ABOUT</a>
        <a href="#performance" class="w3-bar-item w3-button">PERFORMANCE</a>
        <a href="#timeline" class="w3-bar-item w3-button">OUR STORY</a>
        <a href="#spos" class="w3-bar-item w3-button">SPOs</a>
      </div>
      <!-- Hide right-floated links on small screens and replace them with a menu icon -->
  
      <a href="#" class="w3-bar-item w3-button w3-right w3-hide-large w3-hide-medium" on:click={w3_open}>
        <i class="fa fa-bars"></i>
      </a>
    </div>
</div>
  
<!-- Sidebar on small screens when clicking the menu icon -->
<nav class="w3-sidebar w3-bar-block w3-black w3-card w3-animate-left w3-hide-medium w3-hide-large" style="display:none" bind:this={piadaSidebar}>
    <a href="#" on:click={w3_close} class="w3-bar-item w3-button w3-large w3-padding-16">Close ×</a>
    <a href="#about" on:click={w3_close} class="w3-bar-item w3-button">ABOUT</a>
    <a href="#performance" on:click={w3_close} class="w3-bar-item w3-button">PERFORMANCE</a>
    <a href="#timeline" on:click={w3_close} class="w3-bar-item w3-button">OUR STORY</a>
    <a href="#spos" on:click={w3_close} class="w3-bar-item w3-button">SPOs</a>
</nav>

<slot />

<!-- Footer -->
<footer class="w3-center w3-black w3-padding-84">
    <Delegate/>
    <div class="w3-xlarge w3-section">
      <span class="p-p3">&#960; &#43; &#8371; &#61; &#8766;</span>
      <a href="https://twitter.com/Piada_stakePool" rel="noreferrer" target="_blank"><i class="fa-brands fa-twitter w3-hover-opacity p-p3"></i></a>
      <a href="https://t.me/piadapool" rel="noreferrer" target="_blank"><i class="fa-brands fa-telegram w3-hover-opacity p-p3"></i></a>
      <a href="https://armada-alliance.com/" rel="noreferrer" target="_blank"><img class="w3-hover-opacity" src={aaShip} alt="Armada Alliance Logo" style="height:30px;position:relative;top:-1px;"></a>
    </div>
    <p>PIADA - ARM'ed Cardano Stake Pool &#169; 2023<br />This website is running in Svelte on a Raspberry Pi <span style="color: #e60000;"><i class="fa-solid fa-heart" style="padding-left:5px;"></i></span></p>
    
    <p>Pool ID - <a href="https://pooltool.io/pool/b8d8742c7b7b512468448429c776b3b0f824cef460db61aa1d24bc65/awards" target="_blank" rel="noreferrer">b8d8742c7b7b512468448429c776b3b0f824cef460db61aa1d24bc65</a><br />
        Bech32 Pool ID - <a href="https://cexplorer.io/pool/pool1hrv8gtrm0dgjg6zyss5uwa4nkruzfnh5vrdkr2sayj7x2nw6mjc" target="_blank" rel="noreferrer">pool1hrv8gtrm0dgjg6zyss5uwa4nkruzfnh5vrdkr2sayj7x2nw6mjc</a></p>
</footer>