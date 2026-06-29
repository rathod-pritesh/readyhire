<script>
	import { FileText, Trash2, CheckCircle2, FileJson, FileSpreadsheet } from "@lucide/svelte";
	import { fade, slide } from "svelte/transition";

	let { file, onRemove } = $props();

	// Format file size
	const formatBytes = (bytes, decimals = 2) => {
		if (!bytes) return "0 Bytes";
		const k = 1024;
		const dm = decimals < 0 ? 0 : decimals;
		const sizes = ["Bytes", "KB", "MB", "GB"];
		const i = Math.floor(Math.log(bytes) / Math.log(k));
		return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + " " + sizes[i];
	};

	// Determine file icon
	const getFileIcon = (filename) => {
		const ext = filename.split(".").pop().toLowerCase();
		return FileText;
	};

	let FileIcon = $derived(getFileIcon(file.name));
</script>

<div
	transition:slide={{ duration: 300 }}
	class="flex flex-col gap-4 rounded-2xl border border-border bg-card p-5 shadow-sm transition-all duration-300"
>
	<div class="flex items-start justify-between gap-4">
		<div class="flex items-center gap-4 min-w-0">
			<!-- File Icon Wrapper -->
			<div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-[#2E4540]/15 text-[#408175]">
				<FileIcon class="h-6 w-6" />
			</div>

			<!-- Metadata -->
			<div class="min-w-0">
				<p class="truncate font-semibold text-sm text-foreground" title={file.name}>
					{file.name}
				</p>
				<p class="text-xs text-muted-foreground mt-0.5">
					{formatBytes(file.size)}
				</p>
			</div>
		</div>

		<!-- Remove Button -->
		<button
			onclick={onRemove}
			class="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-destructive/10 hover:text-destructive transition-all"
			aria-label="Remove file"
		>
			<Trash2 class="h-4.5 w-4.5" />
		</button>
	</div>

	<!-- Status Indicator -->
	<div class="flex items-center justify-between border-t border-border/40 pt-3 text-xs">
		<div class="flex items-center gap-1.5 text-[#408175] font-medium">
			<CheckCircle2 class="h-4 w-4" />
			<span>Ready for analysis</span>
		</div>
		<span class="text-muted-foreground">Resume parsed</span>
	</div>
</div>
