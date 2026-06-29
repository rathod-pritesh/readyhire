<script>
	import Container from "./Container.svelte";
	import { Sparkles, Code, Globe, Link } from "@lucide/svelte";
</script>

<footer class="border-t border-border/40 bg-background/50 py-12 md:py-16 transition-colors duration-300">
	<Container>
		<div class="grid grid-cols-1 gap-8 sm:grid-cols-2 md:grid-cols-4">
			<!-- Branding -->
			<div class="flex flex-col gap-3 sm:col-span-2">
				<div class="flex items-center gap-2">
					<div class="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-[#2E4540] to-[#408175] text-white">
						<Sparkles class="h-4 w-4" />
					</div>
					<span class="font-bold text-lg text-foreground">ReadyHire</span>
				</div>
				<p class="max-w-xs text-sm text-muted-foreground leading-relaxed">
					Optimize your application with AI-powered resume parsing and ATS keyword analysis. Land your dream job.
				</p>
			</div>

			<!-- Product Links -->
			<div class="flex flex-col gap-3">
				<h3 class="font-semibold text-sm text-foreground uppercase tracking-wider">Product</h3>
				<ul class="space-y-2 text-sm">
					<li><a href="#analyzer" class="text-muted-foreground hover:text-foreground transition-colors">Resume Analyzer</a></li>
					<li><a href="#features" class="text-muted-foreground hover:text-foreground transition-colors">Features</a></li>
					<li><a href="#pricing" class="text-muted-foreground hover:text-foreground transition-colors">Pricing</a></li>
				</ul>
			</div>

			<!-- Connect / Social -->
			<div class="flex flex-col gap-3">
				<h3 class="font-semibold text-sm text-foreground uppercase tracking-wider">Connect</h3>
				<div class="flex items-center gap-4 text-muted-foreground">
					<a href="https://twitter.com" target="_blank" rel="noopener noreferrer" class="hover:text-[#408175] transition-colors" aria-label="Twitter">
						<Globe class="h-5 w-5" />
					</a>
					<a href="https://github.com" target="_blank" rel="noopener noreferrer" class="hover:text-[#408175] transition-colors" aria-label="GitHub">
						<Code class="h-5 w-5" />
					</a>
					<a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="hover:text-[#408175] transition-colors" aria-label="LinkedIn">
						<Link class="h-5 w-5" />
					</a>
				</div>
			</div>
		</div>

		<div class="mt-12 border-t border-border/40 pt-8 flex flex-col sm:flex-row items-center justify-between gap-4">
			<p class="text-xs text-muted-foreground">
				&copy; {new Date().getFullYear()} ReadyHire. All rights reserved.
			</p>
			<div class="flex gap-6 text-xs text-muted-foreground">
				<a href="#privacy" class="hover:text-foreground transition-colors">Privacy Policy</a>
				<a href="#terms" class="hover:text-foreground transition-colors">Terms of Service</a>
			</div>
		</div>
	</Container>
</footer>
