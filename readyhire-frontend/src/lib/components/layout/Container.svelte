<script>
	let { children, class: className = "", ...rest } = $props();
</script>

<div class="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8 {className}" {...rest}>
	{@render children()}
</div>
