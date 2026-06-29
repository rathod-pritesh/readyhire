<script>
	import { UploadCloud, FileText } from "@lucide/svelte";

	// Svelte 5 callback props
	let { onFileSelected, accept = ".pdf,.docx,.txt" } = $props();

	let isDragging = $state(false);
	let fileInputRef = $state(null);

	function handleDragOver(e) {
		e.preventDefault();
		isDragging = true;
	}

	function handleDragLeave() {
		isDragging = false;
	}

	function handleDrop(e) {
		e.preventDefault();
		isDragging = false;
		if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
			const file = e.dataTransfer.files[0];
			if (validateFile(file)) {
				onFileSelected(file);
			}
		}
	}

	function handleFileChange(e) {
		if (e.target.files && e.target.files.length > 0) {
			const file = e.target.files[0];
			if (validateFile(file)) {
				onFileSelected(file);
			}
		}
	}

	function validateFile(file) {
		const extension = file.name.substring(file.name.lastIndexOf(".")).toLowerCase();
		const acceptedExtensions = accept.split(",");
		if (!acceptedExtensions.includes(extension)) {
			alert(`Invalid file type. Please upload one of the following: ${accept}`);
			return false;
		}
		// Max file size: 10MB
		if (file.size > 10 * 1024 * 1024) {
			alert("File is too large. Maximum size is 10MB.");
			return false;
		}
		return true;
	}

	function triggerFileInput() {
		fileInputRef?.click();
	}
</script>

<!-- Drag and drop zone -->
<div
	role="button"
	tabindex="0"
	onclick={triggerFileInput}
	onkeydown={(e) => e.key === "Enter" && triggerFileInput()}
	ondragover={handleDragOver}
	ondragleave={handleDragLeave}
	ondrop={handleDrop}
	class="relative flex flex-col items-center justify-center rounded-2xl border-2 border-dashed p-8 text-center transition-all duration-300 cursor-pointer
		{isDragging
			? 'border-[#408175] bg-[#2E4540]/10 scale-[0.99] shadow-sm shadow-[#2E4540]/20'
			: 'border-border bg-card hover:border-muted-foreground/50 hover:bg-muted/30 dark:hover:bg-muted/10'}
		group"
>
	<!-- Hidden Input -->
	<input
		type="file"
		bind:this={fileInputRef}
		class="hidden"
		{accept}
		onchange={handleFileChange}
	/>

	<!-- Visual Elements -->
	<div class="relative mb-4 flex h-14 w-14 items-center justify-center rounded-xl bg-muted group-hover:scale-110 transition-transform duration-300">
		<UploadCloud class="h-7 w-7 text-muted-foreground group-hover:text-[#408175] transition-colors duration-300" />
	</div>

	<h3 class="mb-1 font-semibold text-base text-foreground tracking-tight">
		Drag & drop your resume
	</h3>
	<p class="mb-4 text-xs text-muted-foreground max-w-xs">
		Supports PDF, DOCX, or TXT (Max 10MB)
	</p>

	<div class="inline-flex h-9 items-center justify-center rounded-lg bg-secondary px-4 text-sm font-medium text-secondary-foreground border border-border shadow-sm hover:bg-secondary/80 hover:text-foreground transition-all">
		Browse Files
	</div>
</div>
