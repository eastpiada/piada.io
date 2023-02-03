<script>
    function handleDelegate() {
      var pool_id = 'b8d8742c7b7b512468448429c776b3b0f824cef460db61aa1d24bc65';
      var blockfrost_project_id = 'mainnetS5mFxtBfFviYRrG9zCW6fJMj9xKKuOIa';
      var link = 'https://armada-alliance.com/delegation-widget?pool_id=' + pool_id + '&blockfrost_project_id=' + blockfrost_project_id;
      var width = 600;
      var height = Math.min(800, window.outerHeight);
      var left = (window.outerWidth / 2) - (width / 2);
      var top = (window.outerHeight - height) / 2;
      window.open(link, 'Delegate', 'width=' + width + ',height=' + height + ',toolbar=0,menubar=0,location=0,status=0,scrollbars=1,resizable=1,left=' + left + ',top=' + top);
    }
    
    function delegateWallet() {
      var link = 'https://cardano-solutions.com/stake?t=MAc0kKV5gRb3DIMkptPbgWsD1GyYFS&wallet=yoroi,flint,nami,eternl,gerowallet';
      var width = 800;
      var height = Math.min(800, window.outerHeight);
      var left = (window.outerWidth / 2) - (width / 2);
      var top = (window.outerHeight - height) / 2;
      window.open(link, 'Delegate', 'width=' + width + ',height=' + height + ',toolbar=0,menubar=0,location=0,status=0,scrollbars=1,resizable=1,left=' + left + ',top=' + top);
    }
</script>

<button type="button" class="w3-button w3-light-grey w3-padding-large w3-large w3-margin-top" on:click={handleDelegate}><i class="fa-solid fa-wallet w3-margin-right"></i>Connect your wallet</button>
<!--<button type="button" class="w3-button w3-light-grey w3-padding-large w3-large w3-margin-top" on:click={delegateWallet}>Delegate!</button>-->