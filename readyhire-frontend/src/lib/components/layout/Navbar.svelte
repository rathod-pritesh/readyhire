<script>
	import Container from "./Container.svelte";
	import { Sun, Moon, Sparkles, Menu, X } from "@lucide/svelte";
	import { onMount } from "svelte";
	import { page } from "$app/stores";

	let isDark = $state(false);
	let isMobileMenuOpen = $state(false);

	onMount(() => {
		// Check local storage or system preference
		const savedTheme = localStorage.getItem("theme");
		if (savedTheme === "dark" || (!savedTheme && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
			isDark = true;
			document.documentElement.classList.add("dark");
		} else {
			isDark = false;
			document.documentElement.classList.remove("dark");
		}
	});

	function toggleTheme() {
		isDark = !isDark;
		if (isDark) {
			document.documentElement.classList.add("dark");
			localStorage.setItem("theme", "dark");
		} else {
			document.documentElement.classList.remove("dark");
			localStorage.setItem("theme", "light");
		}
	}
</script>

<nav class="sticky top-0 z-50 w-full border-b border-border/40 bg-background/80 backdrop-blur-md transition-all duration-300">
	<Container>
		<div class="flex h-16 items-center justify-between">
			<!-- Logo -->
			<div class="flex items-center gap-2">
				<a href="/" class="flex items-center gap-2 font-bold text-xl tracking-tight text-foreground transition-all hover:opacity-90">
					<div class="relative flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-[#2E4540] to-[#408175] text-white shadow-sm shadow-[#2E4540]/30">
						<Sparkles class="h-5 w-5" />
					</div>
					<span class="bg-gradient-to-r from-foreground via-foreground/90 to-muted-foreground bg-clip-text text-transparent">ReadyHire</span>
				</a>
			</div>

			<!-- Desktop Navigation Links -->
			<div class="hidden md:flex items-center gap-8">
				<a href="/features" class="text-sm font-medium transition-colors hover:text-foreground {$page.url.pathname === '/features' ? 'text-foreground underline decoration-[#408175] decoration-2 underline-offset-4 font-semibold' : 'text-muted-foreground'}">Features</a>
				<a href="/how-it-works" class="text-sm font-medium transition-colors hover:text-foreground {$page.url.pathname === '/how-it-works' ? 'text-foreground underline decoration-[#408175] decoration-2 underline-offset-4 font-semibold' : 'text-muted-foreground'}">How It Works</a>
				<a href="/pricing" class="text-sm font-medium transition-colors hover:text-foreground {$page.url.pathname === '/pricing' ? 'text-foreground underline decoration-[#408175] decoration-2 underline-offset-4 font-semibold' : 'text-muted-foreground'}">Pricing</a>
				<a href="/faqs" class="text-sm font-medium transition-colors hover:text-foreground {$page.url.pathname === '/faqs' ? 'text-foreground underline decoration-[#408175] decoration-2 underline-offset-4 font-semibold' : 'text-muted-foreground'}">FAQs</a>
			</div>

			<!-- Action Buttons / Theme Toggle -->
			<div class="hidden md:flex items-center gap-4">
				<button
					onclick={toggleTheme}
					class="relative flex h-9 w-9 items-center justify-center rounded-lg border border-border bg-background text-muted-foreground hover:bg-muted hover:text-foreground transition-all duration-200"
					aria-label="Toggle theme"
				>
					{#if isDark}
						<Sun class="h-[1.2rem] w-[1.2rem] transition-all" />
					{:else}
						<Moon class="h-[1.2rem] w-[1.2rem] transition-all" />
					{/if}
				</button>
				<a
					href="/#analyzer"
					class="inline-flex h-9 items-center justify-center rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/95 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
				>
					Get Started
				</a>
			</div>

			<!-- Mobile Menu Button -->
			<div class="flex items-center gap-2 md:hidden">
				<button
					onclick={toggleTheme}
					class="relative flex h-9 w-9 items-center justify-center rounded-lg border border-border bg-background text-muted-foreground hover:bg-muted hover:text-foreground transition-all"
					aria-label="Toggle theme"
				>
					{#if isDark}
						<Sun class="h-[1.2rem] w-[1.2rem]" />
					{:else}
						<Moon class="h-[1.2rem] w-[1.2rem]" />
					{/if}
				</button>
				<button
					onclick={() => (isMobileMenuOpen = !isMobileMenuOpen)}
					class="flex h-9 w-9 items-center justify-center rounded-lg border border-border bg-background text-muted-foreground hover:bg-muted hover:text-foreground transition-all"
					aria-label="Toggle menu"
				>
					{#if isMobileMenuOpen}
						<X class="h-5 w-5" />
					{:else}
						<Menu class="h-5 w-5" />
					{/if}
				</button>
			</div>
		</div>
	</Container>

	<!-- Mobile Menu -->
	{#if isMobileMenuOpen}
		<div class="border-b border-border/40 bg-background md:hidden">
			<div class="space-y-1 px-4 pb-4 pt-2">
				<a
					href="/features"
					onclick={() => (isMobileMenuOpen = false)}
					class="block rounded-lg px-3 py-2 text-base font-medium transition-colors {$page.url.pathname === '/features' ? 'bg-[#2E4540]/10 text-[#408175] font-semibold' : 'text-muted-foreground hover:bg-muted hover:text-foreground'}"
				>
					Features
				</a>
				<a
					href="/how-it-works"
					onclick={() => (isMobileMenuOpen = false)}
					class="block rounded-lg px-3 py-2 text-base font-medium transition-colors {$page.url.pathname === '/how-it-works' ? 'bg-[#2E4540]/10 text-[#408175] font-semibold' : 'text-muted-foreground hover:bg-muted hover:text-foreground'}"
				>
					How It Works
				</a>
				<a
					href="/pricing"
					onclick={() => (isMobileMenuOpen = false)}
					class="block rounded-lg px-3 py-2 text-base font-medium transition-colors {$page.url.pathname === '/pricing' ? 'bg-[#2E4540]/10 text-[#408175] font-semibold' : 'text-muted-foreground hover:bg-muted hover:text-foreground'}"
				>
					Pricing
				</a>
				<a
					href="/faqs"
					onclick={() => (isMobileMenuOpen = false)}
					class="block rounded-lg px-3 py-2 text-base font-medium transition-colors {$page.url.pathname === '/faqs' ? 'bg-[#2E4540]/10 text-[#408175] font-semibold' : 'text-muted-foreground hover:bg-muted hover:text-foreground'}"
				>
					FAQs
				</a>
				<div class="pt-4 border-t border-border/40">
					<a
						href="/#analyzer"
						onclick={() => (isMobileMenuOpen = false)}
						class="flex w-full items-center justify-center rounded-lg bg-primary px-4 py-2.5 text-center text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/95"
					>
						Get Started
					</a>
				</div>
			</div>
		</div>
	{/if}
</nav>
