<script>
	import { Download, Loader2, CheckCircle2 } from "@lucide/svelte";
	import { fade } from "svelte/transition";

	let isDownloading = $state(false);
	let downloadSuccess = $state(false);

	function triggerDownload() {
		if (isDownloading) return;
		
		isDownloading = true;
		downloadSuccess = false;

		// Mock download process
		setTimeout(() => {
			isDownloading = false;
			downloadSuccess = true;

			// Trigger print stylesheet or actual print dialog for mock exporting
			setTimeout(() => {
				window.print();
			}, 300);

			setTimeout(() => {
				downloadSuccess = false;
			}, 3000);
		}, 1800);
	}
</script>

<div class="flex flex-col items-center justify-between gap-4 rounded-2xl border border-[#408175]/20 bg-[#2E4540]/10 p-6 md:flex-row transition-all duration-300">
	<div class="space-y-1 text-center md:text-left">
		<h4 class="font-bold text-sm text-foreground">Want to save these recommendations?</h4>
		<p class="text-xs text-muted-foreground">Export your comprehensive optimization report, keyword analysis, and cover letter draft.</p>
	</div>

	<button
		onclick={triggerDownload}
		disabled={isDownloading}
		class="inline-flex h-10 items-center justify-center gap-2 rounded-xl bg-[#2E4540] hover:bg-[#408175] disabled:bg-[#2E4540]/50 text-white px-5 py-2.5 text-sm font-semibold shadow-sm shadow-[#2E4540]/30 transition-all select-none w-full md:w-auto shrink-0 cursor-pointer"
	>
		{#if isDownloading}
			<Loader2 class="h-4 w-4 animate-spin" />
			<span>Generating Report PDF...</span>
		{:else}
			{#if downloadSuccess}
				<CheckCircle2 class="h-4 w-4" />
				<span>Report Saved!</span>
			{:else}
				<Download class="h-4 w-4" />
				<span>Download Full Report</span>
			{/if}
		{/if}
	</button>
</div>
