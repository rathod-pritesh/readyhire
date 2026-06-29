<script>
	import DragDropZone from "./DragDropZone.svelte";
	import ResumePreview from "./ResumePreview.svelte";

	let { file = $bindable(null), onFileSelected, onRemove } = $props();

	function handleFileSelected(selectedFile) {
		file = selectedFile;
		if (onFileSelected) {
			onFileSelected(selectedFile);
		}
	}

	function handleRemove() {
		file = null;
		if (onRemove) {
			onRemove();
		}
	}
</script>

<div class="w-full">
	{#if !file}
		<DragDropZone onFileSelected={handleFileSelected} />
	{:else}
		<ResumePreview {file} onRemove={handleRemove} />
	{/if}
</div>
